# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
import logging

logger = logging.getLogger(__name__)


def print_report_footer(passed, failed, skipped, errors, total_time):
    total = passed + failed + skipped + errors
    prefix = 'Passed: %s, Failed: %s, Skipped: %s, Errors: %s -- Total: %s' % (passed, failed, skipped, errors, total)
    suffix = 'Total time: %s second(s)' % total_time
    separator = '\n' + '-' * 120 + '\n'
    logger.info('%s%s%s%s%s' % (separator, prefix, ' ' * (120 - (len(prefix) + len(suffix))), suffix, separator))


def format_outcome(outcome):
    if outcome:
        return 'PASSED'
    else:
        return 'FAILED'


def print_error(error):
    lines = error.splitlines()
    result = '\n'
    max_len = 0
    for line in lines:
        if len(line) > max_len:
            max_len = len(line)
    result = result + '-' * (max_len + 4) + '\n'
    for line in lines:
        result = result + '» ' + line + ' ' * (max_len - len(line)) + ' «' + '\n'
    result = result + '-' * (max_len + 4) + '\n'
    return result


def format_stack(stack):
    result = 'Traceback (most recent call last):\n'
    for line in stack:
        result += '  File "' + str(line[0]) + '", line ' + str(line[1]) + ', in ' + str(line[2]) + '\n    ' + \
                  str(line[3]) + '\n'
    return result


def get_duration(start_time, end_time):
    return round(end_time - start_time, 2)
