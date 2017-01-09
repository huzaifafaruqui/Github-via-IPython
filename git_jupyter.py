import requests
import json
import base64


class Github(object):
    """
    Attributes:
        session: Request.Session() instance
        url: url of api
        r: Response object
        payload: params of request
        sha: SHA of commit
    """
    def __init__(self, owner, repo, username, password):
        """
        Args:
            owner: Repository owner
            repo: Name of repository
            username: Username of owner
            password: Password of owner
        """
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.url = 'https://api.github.com/repos/%s/%s/contents/' % (owner, repo)
        self.r = ''
        self.payload = ''
        self.sha = ''

    def get_contents(self, name=None):
        """List the contents of the repo/file
        Args:
            name: Name of file (Optional)
        """
        if name is None:
            self.r = self.session.get(self.url)
        else:
            self.r = self.session.get(self.url+name)
        if self.r.status_code == 200:
            return self.r.json()
        else:
            self.r.raise_for_status()

    def display_file(self, name):
        """Display the contents of a file.
        Args:
            name: Name of file
        Returns:
            A string which is the content of the file
        """
        self.r = self.get_contents(name)
        return base64.b64decode(self.r['content'])

    def create_file(self, name, message, content):
        """Creates a new file in Github repo
        Args:
            name: Name of new file'
            message: Commit message
            content: Content of commit
        """
        self.payload = json.dumps({'message': message,
                                   'content': base64.b64encode(content)})
        self.r = self.session.put(self.url+name, data=self.payload)
        if self.r.status_code == 201:
            return self.r.json()
        else:
            self.r.raise_for_status()

    def delete_file(self, name, message):
        """Deletes a file
        Args:
            name: Name of new file'
            message: Commit message
        """
        self.sha = self.get_contents(name)['sha']
        self.payload = json.dumps({'message': message, 'sha': self.sha})
        self.r = self.session.delete(self.url+name, data=self.payload)
        if self.r.status_code == 200:
            return self.r.json()
        else:
            self.r.raise_for_status()

    def update_file(self, name, message, content):
        """Updates a file in Github repo
        Args:
            name: Name of the file to be updated
            message: Commit message
            content: Content of commit
        """
        self.sha = self.get_contents(name)['sha']
        self.payload = json.dumps({'message': message,
                                   'content': base64.b64encode(content),
                                   'sha': self.sha})
        r = self.session.put(self.url + name, data=self.payload)
        if r.status_code == 200:
            return r.json()
        else:
            r.raise_for_status()


class Jupyter(Github):
    """Make Github commits in Jupyter IPython notebook
    Attributes:
        content: Content of notebook in string format. Username and password
                github repo is hidden
    """
    def __init__(self, filename, owner, repo, username, password):
        super(Jupyter, self).__init__(owner=owner, repo=repo,
                                      username=username, password=password)
        self.content = ''
        self.filename = filename
        self.username = username
        self.password = password

    def _update_content(self):
        if self.filename.endswith('.ipynb') is False:
            raise NameError('Not an IPython file')
        with open(self.filename, 'r+') as f:
            self.content = f.read()
        self.content = self.content.replace(self.username, '*' * len(self.username))
        self.content = self.content.replace(self.password, '*' * len(self.password))

    def create_file(self, name, message, content=self.content):
        self._update_content()
        super(Jupyter, self).create_file(name=name, message=message,
                                        content=content)

    def update_file(self, name, message, content=self.content):
        self._update_content()
        super(Jupyter, self).update_file(name=name, message=message,
                                         content=content)

    #use Base class method for deletion
