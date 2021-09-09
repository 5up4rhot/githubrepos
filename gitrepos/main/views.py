from django.shortcuts import redirect, render
from .scripts.github import GitHubRequest, GitHubResponse
from .models import Owner, Repo
from rest_framework import viewsets
from .serializers import OwnerHyperlinkedSerializer, RepoHyperlinkedSerializer, OwnerSerializer, RepoSerializer


def save_repo(ids, objs):
    # ids (repo_id, owner_id); entry (repo, owner)
    try:
        owner = Owner.objects.get(id=ids[1])
        print('Owner object with id:', owner.id, 'login:',
              owner.login, 'already exists in db')
    except Owner.DoesNotExist:
        owner_ser = OwnerSerializer(data=objs[1])
        if owner_ser.is_valid():
            owner = owner_ser.save()
            print('Owner object with id:', owner.id,
                  'login:', owner.login, 'saved to db')
        else:
            owner = None
            print('Owner object with id:', ids[1], 'cannot be saved!')
    try:
        repo = Repo.objects.get(id=ids[0])
        print('Repo object with id:', repo.id, 'full_name:',
              repo.full_name, 'already exists in db')
    except Repo.DoesNotExist:
        repo_ser = RepoSerializer(data=objs[0])
        if repo_ser.is_valid():
            repo = repo_ser.save()
            print('Repo object with id:', repo.id,
                  'full_name:', repo.full_name, 'saved to db')
        else:
            repo = None
            print('Repo object with id:', ids[0], 'cannot be saved!')

    return repo, owner


# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'get_public_repos' in request.POST:
            r = GitHubRequest().get_public_repos(request.POST.get('since'))
            if r.status_code == 200:
                batch = GitHubResponse(r.json()).get_repo_batch()
                for entry in batch:
                    save_repo(*entry)
                return redirect('api/')
        elif 'get_org_repos' in request.POST:
            r = GitHubRequest().get_org_repos(request.POST.get('org'))
            if r.status_code == 200:
                batch = GitHubResponse(r.json()).get_repo_batch()
                for entry in batch:
                    repo, owner = save_repo(*entry)
                return redirect(owner)
        elif 'get_user_repos' in request.POST:
            r = GitHubRequest().get_user_repos(request.POST.get('user'))
            if r.status_code == 200:
                batch = GitHubResponse(r.json()).get_repo_batch()
                for entry in batch:
                    repo, owner = save_repo(*entry)
                return redirect(owner)
        elif 'get_specific_repo' in request.POST:
            r = GitHubRequest().get_repo(request.POST.get('owner'),
                                         request.POST.get('repo'))
            if r.status_code == 200:
                batch = GitHubResponse(r.json()).get_repo_batch()
                for entry in batch:
                    repo, owner = save_repo(*entry)
                return redirect(repo)
    return render(request, 'main/index.html')


class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Owner.objects.all().order_by('-id')
    serializer_class = OwnerHyperlinkedSerializer


class RepoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Repo.objects.all().order_by('-id')
    serializer_class = RepoHyperlinkedSerializer
