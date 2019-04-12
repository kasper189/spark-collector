"""A.
"""
import argparse


def parse_input_parameters():
    parser = argparse.ArgumentParser(description='Foo')

    parser.add_argument("-s", "--server", dest='server',
                        help="History Server Name", required=True)
    parser.add_argument("-p", "--port", dest='port',
                        help="History Server Port", required=True)
    parser.add_argument("-a", "--applicationId", dest='appId',
                        help="ApplicationId", required=True)

    parser.add_argument("-u", "--user", dest='user',
                        help="Username", required=False)
    parser.add_argument("-pwd", "--password", dest='password',
                        help="Password", required=False)

    args = parser.parse_args()
    return args
