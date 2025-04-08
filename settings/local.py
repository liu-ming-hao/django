from.base import *



ALLOWED_HOSTS = []





DINGTALK_WEB_HOOK = 'https://oapi.dingtalk.com/robot/send?access_token=2e55053d802ae0cc023b2c3080d3ee0463127c60d893fcec87a3f44cf40cfca0'

import sentry_sdk

sentry_sdk.init(
    dsn="http://4ba3eabd5b92345f60b6d2f14f49b21c@localhost:9000/2",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,

    # performance tracing sample rate, 采样率, 生产环境访问量过大时，建议调小（不用每一个URL请求都记录性能）
    traces_sample_rate=1.0,  #

    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)