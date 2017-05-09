# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DEFAULT_CSP_POLICY = {
        'default-src': ["'self'"],
        'script-src': [
            "'self'",
            "'unsafe-eval'",  # Needed for Charts.js
        ],
        'frame-ancestors': ["'none'"],
        'img-src': [
            "'self'",
            'data:',
        ],
        'object-src': ["'none'"],
        'reflected-xss': ['block'],
        'font-src': [
            "'self'",
            'fonts.gstatic.com',
        ],
        'style-src': [
            "'self'",
            'fonts.googleapis.com',
            "'unsafe-inline'",  # Needed for Charts.js
        ],
 #       'default-src': ["'none'"];
 #       'script-src': ["'self' www.google-analytics.com;img-src www.google-analytics.com;
        }

_CSP_POLICY_STRING = None



def get_csp_policy():
    global _CSP_POLICY_STRING
    if _CSP_POLICY_STRING is not None:
        return _CSP_POLICY_STRING
    if app.config.get('CSP_POLICY'):
        policy = app.config.get('CSP_POLICY')
    elif app.config.get('EXTEND_CSP_POLICY'):
        policy = collections.defaultdict(list)
        for k, v in DEFAULT_CSP_POLICY.iteritems():
            policy[k] = v
        for k, v in app.config.get('EXTEND_CSP_POLICY').iteritems():
            policy[k].extend(v)
    else:
        policy = DEFAULT_CSP_POLICY
    components = []
    for k, v in policy.iteritems():
        sources = ' '.join(v)
        components.append(k + ' ' + sources)
    _CSP_POLICY_STRING = '; '.join(components)
    return _CSP_POLICY_STRING
