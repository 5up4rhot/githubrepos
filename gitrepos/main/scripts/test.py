import json
j = json.loads('{"id":2935646,"node_id":"MDEwOlJlcG9zaXRvcnkyOTM1NjQ2","name":"brackets-app","full_name":"adobe/brackets-app","private":false,"owner":{"login":"adobe","id":476009,"node_id":"MDEyOk9yZ2FuaXphdGlvbjQ3NjAwOQ==","avatar_url":"https://avatars.githubusercontent.com/u/476009?v=4","gravatar_id":"","url":"https://api.github.com/users/adobe","html_url":"https://github.com/adobe","followers_url":"https://api.github.com/users/adobe/followers","following_url":"https://api.github.com/users/adobe/following{/other_user}","gists_url":"https://api.github.com/users/adobe/gists{/gist_id}","starred_url":"https://api.github.com/users/adobe/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/adobe/subscriptions","organizations_url":"https://api.github.com/users/adobe/orgs","repos_url":"https://api.github.com/users/adobe/repos","events_url":"https://api.github.com/users/adobe/events{/privacy}","received_events_url":"https://api.github.com/users/adobe/received_events","type":"Organization","site_admin":false},"html_url":"https://github.com/adobe/brackets-app","description":"Deprecated CEF1-based app shell for Brackets. Use https://github.com/adobe/brackets-shell instead.","fork":false,"url":"https://api.github.com/repos/adobe/brackets-app","forks_url":"https://api.github.com/repos/adobe/brackets-app/forks","keys_url":"https://api.github.com/repos/adobe/brackets-app/keys{/key_id}","collaborators_url":"https://api.github.com/repos/adobe/brackets-app/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/adobe/brackets-app/teams","hooks_url":"https://api.github.com/repos/adobe/brackets-app/hooks","issue_events_url":"https://api.github.com/repos/adobe/brackets-app/issues/events{/number}","events_url":"https://api.github.com/repos/adobe/brackets-app/events","assignees_url":"https://api.github.com/repos/adobe/brackets-app/assignees{/user}","branches_url":"https://api.github.com/repos/adobe/brackets-app/branches{/branch}","tags_url":"https://api.github.com/repos/adobe/brackets-app/tags","blobs_url":"https://api.github.com/repos/adobe/brackets-app/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/adobe/brackets-app/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/adobe/brackets-app/git/refs{/sha}","trees_url":"https://api.github.com/repos/adobe/brackets-app/git/trees{/sha}","statuses_url":"https://api.github.com/repos/adobe/brackets-app/statuses/{sha}","languages_url":"https://api.github.com/repos/adobe/brackets-app/languages","stargazers_url":"https://api.github.com/repos/adobe/brackets-app/stargazers","contributors_url":"https://api.github.com/repos/adobe/brackets-app/contributors","subscribers_url":"https://api.github.com/repos/adobe/brackets-app/subscribers","subscription_url":"https://api.github.com/repos/adobe/brackets-app/subscription","commits_url":"https://api.github.com/repos/adobe/brackets-app/commits{/sha}","git_commits_url":"https://api.github.com/repos/adobe/brackets-app/git/commits{/sha}","comments_url":"https://api.github.com/repos/adobe/brackets-app/comments{/number}","issue_comment_url":"https://api.github.com/repos/adobe/brackets-app/issues/comments{/number}","contents_url":"https://api.github.com/repos/adobe/brackets-app/contents/{+path}","compare_url":"https://api.github.com/repos/adobe/brackets-app/compare/{base}...{head}","merges_url":"https://api.github.com/repos/adobe/brackets-app/merges","archive_url":"https://api.github.com/repos/adobe/brackets-app/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/adobe/brackets-app/downloads","issues_url":"https://api.github.com/repos/adobe/brackets-app/issues{/number}","pulls_url":"https://api.github.com/repos/adobe/brackets-app/pulls{/number}","milestones_url":"https://api.github.com/repos/adobe/brackets-app/milestones{/number}","notifications_url":"https://api.github.com/repos/adobe/brackets-app/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/adobe/brackets-app/labels{/name}","releases_url":"https://api.github.com/repos/adobe/brackets-app/releases{/id}","deployments_url":"https://api.github.com/repos/adobe/brackets-app/deployments","created_at":"2011-12-07T21:01:01Z","updated_at":"2021-07-24T09:56:38Z","pushed_at":"2018-06-13T17:40:42Z","git_url":"git://github.com/adobe/brackets-app.git","ssh_url":"git@github.com:adobe/brackets-app.git","clone_url":"https://github.com/adobe/brackets-app.git","svn_url":"https://github.com/adobe/brackets-app","homepage":"","size":155023,"stargazers_count":497,"watchers_count":497,"language":"C++","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":132,"mirror_url":null,"archived":true,"disabled":false,"open_issues_count":0,"license":{"key":"other","name":"Other","spdx_id":"NOASSERTION","url":null,"node_id":"MDc6TGljZW5zZTA="},"forks":132,"open_issues":0,"watchers":497,"default_branch":"master","temp_clone_token":null,"organization":{"login":"adobe","id":476009,"node_id":"MDEyOk9yZ2FuaXphdGlvbjQ3NjAwOQ==","avatar_url":"https://avatars.githubusercontent.com/u/476009?v=4","gravatar_id":"","url":"https://api.github.com/users/adobe","html_url":"https://github.com/adobe","followers_url":"https://api.github.com/users/adobe/followers","following_url":"https://api.github.com/users/adobe/following{/other_user}","gists_url":"https://api.github.com/users/adobe/gists{/gist_id}","starred_url":"https://api.github.com/users/adobe/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/adobe/subscriptions","organizations_url":"https://api.github.com/users/adobe/orgs","repos_url":"https://api.github.com/users/adobe/repos","events_url":"https://api.github.com/users/adobe/events{/privacy}","received_events_url":"https://api.github.com/users/adobe/received_events","type":"Organization","site_admin":false},"network_count":132,"subscribers_count":70}')

overlap_fields = {
    'owner': ['id', 'login', 'html_url'],
    'repo': ['id', 'full_name', 'private', 'html_url', 'created_at']
}

pre_owner = j['owner']
owner = {'info': {}}

for k in pre_owner.keys():
    if k in overlap_fields['owner']:
        owner[k] = pre_owner[k]
    elif k == 'type':
        owner[k] = 'USR' if pre_owner[k] == 'User' else 'ORG'
    else:
        owner['info'] |= {k: pre_owner[k]}

print(owner['info'])
print(owner)
