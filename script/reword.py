"""
a script for mitmproxy
https://github.com/mitmproxy/mitmproxy
"""
from mitmproxy import http, ctx


def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
    # flow.request.headers["myheader"] = "value"
    # print('script')

    # _log(flow.request.pretty_url)
    if flow.request.pretty_url.__contains__("supra.tw"):
        _log("match: " + flow.request.pretty_url)
        # flow.response = http.HTTPResponse.make(
        #     200,  # (optional) status code
        #     b"Hello World",  # (optional) content
        #     {"Content-Type": "text/html"}  # (optional) headers
        # )


def response(flow: http.HTTPFlow):
    """
        The full HTTP response has been read.
    """


def _log(msg: str):
    ctx.log.info("script => " + msg)


def main():
    return


if __name__ == '__main__':
    main()
