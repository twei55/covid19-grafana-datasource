# pylint: disable=no-member
import json
from mamba import before, describe, it
from expects import contain, expect, have_keys

from src.app import app

with describe("App") as self:

    with before.each:
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    with describe("/search") as self:

        with before.each:
            self.response = self.client.get('/search')

        with it("returns list of metrics"):
            expect(json.loads(self.response.data)).to(
                contain('Germany:confirmed', 'Germany:deaths', 'Germany:recovered')
            )

    with describe("/query") as self:

        with before.each:
            post_params_header = {"Content-Type": "application/json"}
            post_params_body = {
                "range": {
                    "from": "2020-01-22T00:00:00.000Z",
                    "to": "2020-03-19T00:00:00.000Z"
                },
                "targets": [
                    {"target": "Italy:confirmed", "refId": "A", "type": "timeseries"}
                ]
            }
            self.response = self.client.post(
                '/query',
                headers=post_params_header,
                json=post_params_body)

        with it("returns list of metrics"):
            expect(json.loads(self.response.data)[0]).to(
                have_keys('target', 'datapoints')
            )
