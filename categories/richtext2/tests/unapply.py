#!/usr/bin/python2.5
#
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the 'License')
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""UnApply tests"""

__author__ = 'rolandsteiner@google.com (Roland Steiner)'

# Result selection should continue to wrap the originally selected HTML (if any).
# Result selection should be inside any newly created element.
# A selection that started as a text selection should remain a text selection.
# Elements that are not or only partially selected should retain their name and attributes.

# Non-"styleWithCSS" tests: "styleWithCSS" should have no bearing on the unapply operation.

UNAPPLY_TESTS = {
  'id':            'U',
  'caption':       'Unapply Existing Formatting Tests',
  'checkAttrs':    True,
  'checkStyle':    True,
  'styleWithCSS':  False,
  'expected':      'foo[bar]baz',

  'RFC': [
    # unlink
    { 'id':          'UNLINK-1',
      'desc':        'unlink wrapped <a> element',
      'command':     'unlink',
      'pad':         'foo[<a>bar</a>]baz' },

    { 'id':          'UNLINK-2',
      'desc':        'unlink <a> element where the selection wraps the full content',
      'command':     'unlink',
      'pad':         'foo<a>[bar]</a>baz' },

    { 'id':          'UNLINK-5',
      'desc':        'unlink wrapped <a> element that has a name and href attribute',
      'command':     'unlink',
      'pad':         'foo[<a name="A" href="#U-UNLINK-1">bar</a>]baz' },

    { 'id':          'UNLINK-6',
      'desc':        'unlink contained <a> element',
      'command':     'unlink',
      'pad':         'foo[b<a>a</a>r]baz' },

    { 'id':          'UNLINK-7',
      'desc':        'unlink 2 contained <a> elements',
      'command':     'unlink',
      'pad':         'foo[<a>b</a>a<a>r</a>]baz' }
  ],
    
  'Proposed': [
    # bold
    { 'id':          'B-B-1-SI',
      'desc':        'Selection within tags; remove <b> tags',
      'command':     'bold',
      'pad':         'foo<b>[bar]</b>baz' },

    { 'id':          'B-B-SO-1',
      'desc':        'Selection outside of tags; remove <b> tags',
      'command':     'bold',
      'pad':         'foo[<b>bar</b>]baz' },

    { 'id':          'B-B-SM-1',
      'desc':        'Selection mixed; remove <b> tags',
      'command':     'bold',
      'pad':         'foo[<b>bar]</b>baz' },

    { 'id':          'B-B-SM-2',
      'desc':        'Selection mixed; remove <b> tags',
      'command':     'bold',
      'pad':         'foo<b>[bar</b>]baz' },

    { 'id':          'B-STRONG-1-SI',
      'desc':        'Selection within tags; remove <strong> tags',
      'command':     'bold',
      'pad':         'foo<strong>[bar]</strong>baz' },

    { 'id':          'B-STRONG-1-SO',
      'desc':        'Selection outside of tags; remove <strong> tags',
      'command':     'bold',
      'pad':         'foo[<strong>bar</strong>]baz' },

    { 'id':          'B-STRONG-1-SL',
      'desc':        'Selection mixed; remove <strong> tags',
      'command':     'bold',
      'pad':         'foo[<strong>bar]</strong>baz' },

    { 'id':          'B-STRONG-1-SR',
      'desc':        'Selection mixed; remove <strong> tags',
      'command':     'bold',
      'pad':         'foo<strong>[bar</strong>]baz' },

    { 'id':          'B-STYLE-FW-1-SI',
      'desc':        'Selection within tags; remove "font-weight: bold"',
      'command':     'bold',
      'pad':         'foo<span style="font-weight: bold">[bar]</span>baz' },

    { 'id':          'B-STYLE-FW-1-SO',
      'desc':        'Selection outside of tags; remove "font-weight: bold"',
      'command':     'bold',
      'pad':         'foo[<span style="font-weight: bold">bar</span>]baz' },

    { 'id':          'B-STYLE-FW-1-SL',
      'desc':        'Selection mixed; remove "font-weight: bold"',
      'command':     'bold',
      'pad':         'foo[<span style="font-weight: bold">bar]</span>baz' },

    { 'id':          'B-STYLE-FW-1-SR',
      'desc':        'Selection mixed; remove "font-weight: bold"',
      'command':     'bold',
      'pad':         'foo<span style="font-weight: bold">[bar</span>]baz' },

    # italic
    { 'id':          'I-I-1-SI',
      'desc':        'Selection within tags; remove <i> tags',
      'command':     'italic',
      'pad':         'foo<i>[bar]</i>baz' },

    { 'id':          'I-I-1O',
      'desc':        'Selection outside of tags; remove <i> tags',
      'command':     'italic',
      'pad':         'foo[<i>bar</i>]baz' },

    { 'id':          'I-I-1-SL',
      'desc':        'Selection mixed; remove <i> tags',
      'command':     'italic',
      'pad':         'foo[<i>bar]</i>baz' },

    { 'id':          'I-I-1-SR',
      'desc':        'Selection mixed; remove <i> tags',
      'command':     'italic',
      'pad':         'foo<i>[bar</i>]baz' },

    { 'id':          'I-EM-1-SI',
      'desc':        'Selection within tags; remove <em> tags',
      'command':     'italic',
      'pad':         'foo<em>[bar]</em>baz' },

    { 'id':          'I-EM-1-SO',
      'desc':        'Selection outside of tags; remove <em> tags',
      'command':     'italic',
      'pad':         'foo[<em>bar</em>]baz' },

    { 'id':          'I-EM-1-SL',
      'desc':        'Selection mixed; remove <em> tags',
      'command':     'italic',
      'pad':         'foo[<em>bar]</em>baz' },

    { 'id':          'I-EM-1-SR',
      'desc':        'Selection mixed; remove <em> tags',
      'command':     'italic',
      'pad':         'foo<em>[bar</em>]baz' },

    { 'id':          'I-STYLE-FS-1-SI',
      'desc':        'Selection within tags; remove "font-style: italic"',
      'command':     'italic',
      'pad':         'foo<span style="font-style: italic">[bar]</span>baz' },

    { 'id':          'I-STYLE-FS-1-SO',
      'desc':        'Selection outside of tags; Italicize "font-style: italic"',
      'command':     'italic',
      'pad':         'foo[<span style="font-style: italic">bar</span>]baz' },

    { 'id':          'I-STYLE-FS-1-SL',
      'desc':        'Selection mixed; Italicize "font-style: italic"',
      'command':     'italic',
      'pad':         'foo[<span style="font-style: italic">bar]</span>baz' },

    { 'id':          'I-STYLE-FS-1-SR',
      'desc':        'Selection mixed; Italicize "font-style: italic"',
      'command':     'italic',
      'pad':         'foo<span style="font-style: italic">[bar</span>]baz' },

    # underline
    { 'id':          'U-U-1-SI',
      'desc':        'Selection within tags; remove <u> tags',
      'command':     'underline',
      'pad':         'foo<u>[bar]</u>baz' },

    { 'id':          'U-U-1-SO',
      'desc':        'Selection outside of tags; remove <u> tags',
      'command':     'underline',
      'pad':         'foo[<u>bar</u>]baz' },

    { 'id':          'U-U-1-SL',
      'desc':        'Selection mixed; remove <u> tags',
      'command':     'underline',
      'pad':         'foo[<u>bar]</u>baz' },

    { 'id':          'U-U-1-SR',
      'desc':        'Selection mixed; remove <u> tags',
      'command':     'underline',
      'pad':         'foo<u>[bar</u>]baz' },

    { 'id':          'U-STYLE-TD-1-SI',
      'desc':        'Selection within tags; remove "text-decoration: underline"',
      'command':     'underline',
      'pad':         'foo<span style="text-decoration: underline">[bar]</span>baz' },

    { 'id':          'U-STYLE-TD-1-SO',
      'desc':        'Selection outside of tags; remove "text-decoration: underline"',
      'command':     'underline',
      'pad':         'foo[<span style="text-decoration: underline">bar</span>]baz' },

    { 'id':          'U-STYLE-TD-1-SL',
      'desc':        'Selection mixed; remove "text-decoration: underline"',
      'command':     'underline',
      'pad':         'foo[<span style="text-decoration: underline">bar]</span>baz' },

    { 'id':          'U-STYLE-TD-1-SR',
      'desc':        'Selection mixed; remove "text-decoration: underline"',
      'command':     'underline',
      'pad':         'foo<span style="text-decoration: underline">[bar</span>]baz' },

    # strikethrough
    { 'id':          'S-S-1-SI',
      'desc':        'Selection within tags; remove <s> tags',
      'command':     'strikethrough',
      'pad':         'foo<s>[bar]</s>baz' },

    { 'id':          'S-S-1-SO',
      'desc':        'Selection outside of tags; remove <s> tags',
      'command':     'strikethrough',
      'pad':         'foo[<s>bar</s>]baz' },

    { 'id':          'S-S-1-SL',
      'desc':        'Selection mixed; remove <s> tags',
      'command':     'strikethrough',
      'pad':         'foo[<s>bar]</s>baz' },

    { 'id':          'S-S-1-SR',
      'desc':        'Selection mixed; remove <s> tags',
      'command':     'strikethrough',
      'pad':         'foo<s>[bar</s>]baz' },

    { 'id':          'S-STRIKE-1-SI',
      'desc':        'Selection within tags; remove <strike> tags',
      'command':     'strikethrough',
      'pad':         'foo<strike>[bar]</strike>baz' },

    { 'id':          'S-STRIKE-1-SO',
      'desc':        'Selection outside of tags; remove <strike> tags',
      'command':     'strikethrough',
      'pad':         'foo[<strike>bar</strike>]baz' },

    { 'id':          'S-STRIKE-1-SL',
      'desc':        'Selection mixed; remove <strike> tags',
      'command':     'strikethrough',
      'pad':         'foo[<strike>bar]</strike>baz' },

    { 'id':          'S-STRIKE-2-SR',
      'desc':        'Selection mixed; remove <strike> tags',
      'command':     'strikethrough',
      'pad':         'foo<strike>[bar</strike>]baz' },

    { 'id':          'S-STYLE-TD-LT-1-SI',
      'desc':        'Selection within tags; remove "text-decoration:line-through"',
      'command':     'strikethrough',
      'pad':         'foo<span style="text-decoration:line-through">[bar]</span>baz' },

    { 'id':          'S-STYLE-TD-LT-1-SO',
      'desc':        'Selection outside of tags; Italicize "text-decoration:line-through"',
      'command':     'strikethrough',
      'pad':         'foo[<span style="text-decoration:line-through">bar</span>]baz' },

    { 'id':          'S-STYLE-TD-LT-1-SL',
      'desc':        'Selection mixed; Italicize "text-decoration:line-through"',
      'command':     'strikethrough',
      'pad':         'foo[<span style="text-decoration:line-through">bar]</span>baz' },

    { 'id':          'S-STYLE-TD-LT-1-SR',
      'desc':        'Selection mixed; Italicize "text-decoration:line-through"',
      'command':     'strikethrough',
      'pad':         'foo<span style="text-decoration:line-through">[bar</span>]baz' },

    # unlink
    { 'id':          'UNLINK-3',
      'desc':        'unlink an <a> element that contains the collapsed selection',
      'command':     'unlink',
      'pad':         'foo<a>ba^r</a>baz',
      'expected':    'fooba^rbaz' },

    { 'id':          'UNLINK-4',
      'desc':        'unlink an <a> element that contains the whole selection',
      'command':     'unlink',
      'pad':         'foo<a>b[a]r</a>baz',
      'expected':    'foob[a]rbaz' },

    { 'id':          'UNLINK-SM-1',
      'desc':        'unlink a partially contained <a> element',
      'command':     'unlink',
      'pad':         'foo[ba<a>r]ba</a>z' },

    { 'id':          'UNLINK-SM-2',
      'desc':        'unlink a partially contained <a> element',
      'command':     'unlink',
      'pad':         'fo<a>o[ba</a>r]baz' }
  ]
};
