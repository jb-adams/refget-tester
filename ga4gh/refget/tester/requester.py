import requests

# makes requests
class Requester(object):

    def __init__(self, url_template, seqid, params, headers):
        self.url_template = url_template
        self.seqid = seqid
        self.params = params
        self.headers = headers

    def format_url(self):
        url = self.url_template
        if self.seqid:
            url = self.url_template.format(seqid=self.seqid)
        return url

    def make_request(self):
        return requests.get(
            self.format_url(),
            params=self.params,
            headers=self.headers
        )
