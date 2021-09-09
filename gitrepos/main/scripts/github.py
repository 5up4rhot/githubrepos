import requests


class GitHubRequest:
    api_url = 'https://api.github.com/'
    headers = {
        'accept': 'application/vnd.github.v3+json'
    }

    def get_public_repos(self, since):
        url = self.api_url+'repositories'
        r = requests.get(url, params={'since': since}, headers=self.headers)
        return r

    def get_org_repos(self, org):
        url = self.api_url+'orgs/'+org+'/repos'
        r = requests.get(url, headers=self.headers)
        return r

    def get_user_repos(self, user):
        url = self.api_url+'users/'+user+'/repos'
        r = requests.get(url, headers=self.headers)
        return r

    def get_repo(self, owner, repo):
        url = self.api_url+'repos/'+owner+'/'+repo
        r = requests.get(url, headers=self.headers)
        return r


class GitHubResponse:
    overlap_fields = {
        'owner': ['id', 'login', 'html_url'],
        'repo': ['id', 'full_name', 'private', 'html_url', 'created_at']
    }

    def __init__(self, data):
        self.data = data

    def get_owner_obj(self, owner_entry):
        owner = {'info': {}}
        for k in owner_entry.keys():
            if k in self.overlap_fields['owner']:
                owner[k] = owner_entry[k]
            elif k == 'type':
                owner[k] = 'USR' if owner_entry[k] == 'User' else 'ORG'
            else:
                owner['info'] |= {k: owner_entry[k]}
        return owner

    def get_repo_obj(self, entry):
        repo = {'info': {}}
        for k in entry.keys():
            if k in self.overlap_fields['repo']:
                repo[k] = entry[k]
            elif k == 'owner':
                owner = self.get_owner_obj(entry[k])
                repo[k] = entry[k]['id']
            else:
                repo['info'] |= {k: entry[k]}
        return repo, owner

    @staticmethod
    def get_ids(entry):
        repo_id = entry['id']
        owner_id = entry['owner']['id']
        return repo_id, owner_id

    def get_repo_batch(self):
        repos = []
        if type(self.data) is list:
            for entry in self.data:
                repos.append((self.get_ids(entry), self.get_repo_obj(entry)))
        else:
            repos.append((self.get_ids(self.data),
                         self.get_repo_obj(self.data)))
        return repos
