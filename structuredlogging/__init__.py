import datetime
import json
import logging
import time
import uuid

import six

class CustomFormatter(logging.Formatter):
    def format(self, record):
        super(CustomFormatter, self).format(record)

        structured = {
            "@timestamp": datetime.datetime.fromtimestamp(record.created).isoformat(),
            "@metadata": {k: getattr(record, k) for k in ["filename", "funcName", "lineno", "module", "pathname", "process", "processName", "thread", "threadName"]},
            "level": record.levelname,
            "messageId": str(uuid.uuid4())
        }

        if isinstance(record.msg, dict):
            structured.update(record.msg)
        elif isinstance(record.msg, six.string_types):
            structured.update({
                "messageTemplate": record.msg,
                "fields": record.args,
            })

            if isinstance(record.args, dict):
                structured["message"] = record.msg.format(**record.args)
            else:
                structured["message"] = record.message
        else:
            structured.update({
                "raw_msg": record.msg,
                "raw_args": record.args,
            })
        
        return json.dumps(structured)