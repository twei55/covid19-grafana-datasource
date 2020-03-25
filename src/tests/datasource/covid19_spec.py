from mamba import before, describe, it
from expects import contain, equal, expect, have_length

from src.datasource.covid19 import Covid19

with describe("Covid19") as self:

    with before.each:
        self.covid19 = Covid19()

    with describe("#countries") as self:

        with it("returns all country names"):
            expect(self.covid19.countries()).to(contain(
                'Italy', 'Germany'
            ))

    with describe("#metrics") as self:

        with it("returns three metrics for every country"):
            expect(self.covid19.metrics()).to(contain(
                'Italy:confirmed', 'Italy:deaths', 'Italy:recovered',
                'Germany:confirmed', 'Germany:deaths', 'Germany:recovered',
            ))

    with describe("#timeseries") as self:
        with it("returns 58 datapoints for group 'confirmed'"):
            expect(self.covid19.timeseries(
                "Italy:confirmed",
                "2020-01-22T00:00:00.000Z",
                "2020-03-20T00:00:00.000Z"
            )).to(have_length(59))

        with it("returns 57 datapoints for group 'deaths'"):
            expect(self.covid19.timeseries(
                "Italy:deaths",
                "2020-01-22T00:00:00.000Z",
                "2020-03-18T00:00:00.000Z"
            )).to(have_length(57))

        with it("returns 40 datapoints for group 'recovered'"):
            expect(self.covid19.timeseries(
                "Italy:recovered",
                "2020-01-22T00:00:00.000Z",
                "2020-03-01T00:00:00.000Z"
            )).to(have_length(40))

        with it("returns one datapoint"):
            expect(self.covid19.timeseries(
                "Italy:confirmed",
                "2020-03-20T00:00:00.000Z",
                "2020-03-20T00:00:00.000Z"
            )).to(have_length(1))

        with it("contains a datapoint set to 0 if key is not present"):
            expect(self.covid19.timeseries(
                "Italy:recovered",
                "2020-03-20T00:00:00.000Z",
                "2020-03-20T00:00:00.000Z"
            )[0][0]).to(equal(0))
