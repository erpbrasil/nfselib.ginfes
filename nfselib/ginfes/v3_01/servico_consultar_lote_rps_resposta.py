#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py version 2.36.6.
# Python 3.8.5 (default, Jul 27 2020, 08:42:51)  [GCC 10.1.0]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('--no-dates', '')
#   ('--member-specs', 'list')
#   ('--use-getter-setter', 'none')
#   ('-f', '')
#   ('-o', '/home/mileo/Projects/erpbrasil/nfselib.ginfes/ginfeslib/v3_01/servico_consultar_lote_rps_resposta.py')
#
# Command line arguments:
#   /tmp/generated/schemas/ginfes/v3_01/servico_consultar_lote_rps_resposta_v03.xsd
#
# Command line:
#   /home/mileo/Projects/erpbrasil/bin/generateDS.py --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f -o "/home/mileo/Projects/erpbrasil/nfselib.ginfes/ginfeslib/v3_01/servico_consultar_lote_rps_resposta.py" /tmp/generated/schemas/ginfes/v3_01/servico_consultar_lote_rps_resposta_v03.xsd
#
# Current working directory (os.getcwd()):
#   v3_01
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from .generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from .generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class ConsultarLoteRpsResposta(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('ListaNfse', 'ListaNfseType', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ListaNfse', 'type': 'ListaNfseType'}, 1),
        MemberSpec_('ListaMensagemRetorno', 'ListaMensagemRetorno', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ListaMensagemRetorno', 'ref': 'ListaMensagemRetorno', 'type': 'ListaMensagemRetorno'}, 1),
    ]
    subclass = None
    superclass = None
    def __init__(self, ListaNfse=None, ListaMensagemRetorno=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ListaNfse = ListaNfse
        self.ListaNfse_nsprefix_ = None
        self.ListaMensagemRetorno = ListaMensagemRetorno
        self.ListaMensagemRetorno_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConsultarLoteRpsResposta)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConsultarLoteRpsResposta.subclass:
            return ConsultarLoteRpsResposta.subclass(*args_, **kwargs_)
        else:
            return ConsultarLoteRpsResposta(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.ListaNfse is not None or
            self.ListaMensagemRetorno is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ConsultarLoteRpsResposta', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConsultarLoteRpsResposta')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConsultarLoteRpsResposta':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConsultarLoteRpsResposta')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConsultarLoteRpsResposta', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConsultarLoteRpsResposta'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ConsultarLoteRpsResposta', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ListaNfse is not None:
            namespaceprefix_ = self.ListaNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaNfse_nsprefix_) else ''
            self.ListaNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaNfse', pretty_print=pretty_print)
        if self.ListaMensagemRetorno is not None:
            namespaceprefix_ = self.ListaMensagemRetorno_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaMensagemRetorno_nsprefix_) else ''
            self.ListaMensagemRetorno.export(outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='ListaMensagemRetorno', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ListaNfse':
            obj_ = ListaNfseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaNfse = obj_
            obj_.original_tagname_ = 'ListaNfse'
        elif nodeName_ == 'ListaMensagemRetorno':
            obj_ = ListaMensagemRetorno.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaMensagemRetorno = obj_
            obj_.original_tagname_ = 'ListaMensagemRetorno'
# end class ConsultarLoteRpsResposta


class tcCpfCnpj(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Cpf', ['tsCpf', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Cpf', 'type': 'xsd:string'}, 2),
        MemberSpec_('Cnpj', ['tsCnpj', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Cnpj', 'type': 'xsd:string'}, 2),
    ]
    subclass = None
    superclass = None
    def __init__(self, Cpf=None, Cnpj=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Cpf = Cpf
        self.validate_tsCpf(self.Cpf)
        self.Cpf_nsprefix_ = None
        self.Cnpj = Cnpj
        self.validate_tsCnpj(self.Cnpj)
        self.Cnpj_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCpfCnpj)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCpfCnpj.subclass:
            return tcCpfCnpj.subclass(*args_, **kwargs_)
        else:
            return tcCpfCnpj(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCpf(self, value):
        result = True
        # Validate type tsCpf, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsCpf' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsCnpj(self, value):
        result = True
        # Validate type tsCnpj, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsCnpj' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Cpf is not None or
            self.Cnpj is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcCpfCnpj', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCpfCnpj')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCpfCnpj':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCpfCnpj')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCpfCnpj', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCpfCnpj'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcCpfCnpj', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cpf is not None:
            namespaceprefix_ = self.Cpf_nsprefix_ + ':' if (UseCapturedNS_ and self.Cpf_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCpf>%s</%sCpf>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cpf), input_name='Cpf')), namespaceprefix_ , eol_))
        if self.Cnpj is not None:
            namespaceprefix_ = self.Cnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnpj_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnpj>%s</%sCnpj>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cnpj), input_name='Cnpj')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Cpf':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cpf')
            value_ = self.gds_validate_string(value_, node, 'Cpf')
            self.Cpf = value_
            self.Cpf_nsprefix_ = child_.prefix
            # validate type tsCpf
            self.validate_tsCpf(self.Cpf)
        elif nodeName_ == 'Cnpj':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnpj')
            value_ = self.gds_validate_string(value_, node, 'Cnpj')
            self.Cnpj = value_
            self.Cnpj_nsprefix_ = child_.prefix
            # validate type tsCnpj
            self.validate_tsCnpj(self.Cnpj)
# end class tcCpfCnpj


class tcEndereco(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Endereco', ['tsEndereco', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Endereco', 'type': 'xsd:string'}, None),
        MemberSpec_('Numero', ['tsNumeroEndereco', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Numero', 'type': 'xsd:string'}, None),
        MemberSpec_('Complemento', ['tsComplementoEndereco', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Complemento', 'type': 'xsd:string'}, None),
        MemberSpec_('Bairro', ['tsBairro', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Bairro', 'type': 'xsd:string'}, None),
        MemberSpec_('CodigoMunicipio', ['tsCodigoMunicipioIbge', 'xsd:int'], 0, 1, {'minOccurs': '0', 'name': 'CodigoMunicipio', 'type': 'xsd:int'}, None),
        MemberSpec_('Uf', ['tsUf', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Uf', 'type': 'xsd:string'}, None),
        MemberSpec_('Cep', ['tsCep', 'xsd:int'], 0, 1, {'minOccurs': '0', 'name': 'Cep', 'type': 'xsd:int'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Endereco=None, Numero=None, Complemento=None, Bairro=None, CodigoMunicipio=None, Uf=None, Cep=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Endereco = Endereco
        self.validate_tsEndereco(self.Endereco)
        self.Endereco_nsprefix_ = None
        self.Numero = Numero
        self.validate_tsNumeroEndereco(self.Numero)
        self.Numero_nsprefix_ = None
        self.Complemento = Complemento
        self.validate_tsComplementoEndereco(self.Complemento)
        self.Complemento_nsprefix_ = None
        self.Bairro = Bairro
        self.validate_tsBairro(self.Bairro)
        self.Bairro_nsprefix_ = None
        self.CodigoMunicipio = CodigoMunicipio
        self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
        self.CodigoMunicipio_nsprefix_ = None
        self.Uf = Uf
        self.validate_tsUf(self.Uf)
        self.Uf_nsprefix_ = None
        self.Cep = Cep
        self.validate_tsCep(self.Cep)
        self.Cep_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcEndereco)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcEndereco.subclass:
            return tcEndereco.subclass(*args_, **kwargs_)
        else:
            return tcEndereco(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsEndereco(self, value):
        result = True
        # Validate type tsEndereco, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 125:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsNumeroEndereco(self, value):
        result = True
        # Validate type tsNumeroEndereco, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsNumeroEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsNumeroEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsComplementoEndereco(self, value):
        result = True
        # Validate type tsComplementoEndereco, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsComplementoEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsComplementoEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsBairro(self, value):
        result = True
        # Validate type tsBairro, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsBairro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsBairro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsCodigoMunicipioIbge(self, value):
        result = True
        # Validate type tsCodigoMunicipioIbge, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsCodigoMunicipioIbge' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsUf(self, value):
        result = True
        # Validate type tsUf, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsUf' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsCep(self, value):
        result = True
        # Validate type tsCep, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsCep' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Endereco is not None or
            self.Numero is not None or
            self.Complemento is not None or
            self.Bairro is not None or
            self.CodigoMunicipio is not None or
            self.Uf is not None or
            self.Cep is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcEndereco', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcEndereco')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcEndereco':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcEndereco')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcEndereco', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcEndereco'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcEndereco', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Endereco is not None:
            namespaceprefix_ = self.Endereco_nsprefix_ + ':' if (UseCapturedNS_ and self.Endereco_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEndereco>%s</%sEndereco>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Endereco), input_name='Endereco')), namespaceprefix_ , eol_))
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Numero), input_name='Numero')), namespaceprefix_ , eol_))
        if self.Complemento is not None:
            namespaceprefix_ = self.Complemento_nsprefix_ + ':' if (UseCapturedNS_ and self.Complemento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sComplemento>%s</%sComplemento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Complemento), input_name='Complemento')), namespaceprefix_ , eol_))
        if self.Bairro is not None:
            namespaceprefix_ = self.Bairro_nsprefix_ + ':' if (UseCapturedNS_ and self.Bairro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBairro>%s</%sBairro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Bairro), input_name='Bairro')), namespaceprefix_ , eol_))
        if self.CodigoMunicipio is not None:
            namespaceprefix_ = self.CodigoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoMunicipio>%s</%sCodigoMunicipio>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoMunicipio, input_name='CodigoMunicipio'), namespaceprefix_ , eol_))
        if self.Uf is not None:
            namespaceprefix_ = self.Uf_nsprefix_ + ':' if (UseCapturedNS_ and self.Uf_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUf>%s</%sUf>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Uf), input_name='Uf')), namespaceprefix_ , eol_))
        if self.Cep is not None:
            namespaceprefix_ = self.Cep_nsprefix_ + ':' if (UseCapturedNS_ and self.Cep_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCep>%s</%sCep>%s' % (namespaceprefix_ , self.gds_format_integer(self.Cep, input_name='Cep'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Endereco':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Endereco')
            value_ = self.gds_validate_string(value_, node, 'Endereco')
            self.Endereco = value_
            self.Endereco_nsprefix_ = child_.prefix
            # validate type tsEndereco
            self.validate_tsEndereco(self.Endereco)
        elif nodeName_ == 'Numero':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Numero')
            value_ = self.gds_validate_string(value_, node, 'Numero')
            self.Numero = value_
            self.Numero_nsprefix_ = child_.prefix
            # validate type tsNumeroEndereco
            self.validate_tsNumeroEndereco(self.Numero)
        elif nodeName_ == 'Complemento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Complemento')
            value_ = self.gds_validate_string(value_, node, 'Complemento')
            self.Complemento = value_
            self.Complemento_nsprefix_ = child_.prefix
            # validate type tsComplementoEndereco
            self.validate_tsComplementoEndereco(self.Complemento)
        elif nodeName_ == 'Bairro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Bairro')
            value_ = self.gds_validate_string(value_, node, 'Bairro')
            self.Bairro = value_
            self.Bairro_nsprefix_ = child_.prefix
            # validate type tsBairro
            self.validate_tsBairro(self.Bairro)
        elif nodeName_ == 'CodigoMunicipio' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoMunicipio')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoMunicipio')
            self.CodigoMunicipio = ival_
            self.CodigoMunicipio_nsprefix_ = child_.prefix
            # validate type tsCodigoMunicipioIbge
            self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
        elif nodeName_ == 'Uf':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Uf')
            value_ = self.gds_validate_string(value_, node, 'Uf')
            self.Uf = value_
            self.Uf_nsprefix_ = child_.prefix
            # validate type tsUf
            self.validate_tsUf(self.Uf)
        elif nodeName_ == 'Cep' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Cep')
            ival_ = self.gds_validate_integer(ival_, node, 'Cep')
            self.Cep = ival_
            self.Cep_nsprefix_ = child_.prefix
            # validate type tsCep
            self.validate_tsCep(self.Cep)
# end class tcEndereco


class tcContato(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Telefone', ['tsTelefone', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Telefone', 'type': 'xsd:string'}, None),
        MemberSpec_('Email', ['tsEmail', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Email', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Telefone=None, Email=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Telefone = Telefone
        self.validate_tsTelefone(self.Telefone)
        self.Telefone_nsprefix_ = None
        self.Email = Email
        self.validate_tsEmail(self.Email)
        self.Email_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcContato)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcContato.subclass:
            return tcContato.subclass(*args_, **kwargs_)
        else:
            return tcContato(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsTelefone(self, value):
        result = True
        # Validate type tsTelefone, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsTelefone' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsTelefone' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsEmail(self, value):
        result = True
        # Validate type tsEmail, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 80:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsEmail' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsEmail' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Telefone is not None or
            self.Email is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcContato', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcContato')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcContato':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcContato')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcContato', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcContato'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcContato', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Telefone is not None:
            namespaceprefix_ = self.Telefone_nsprefix_ + ':' if (UseCapturedNS_ and self.Telefone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTelefone>%s</%sTelefone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Telefone), input_name='Telefone')), namespaceprefix_ , eol_))
        if self.Email is not None:
            namespaceprefix_ = self.Email_nsprefix_ + ':' if (UseCapturedNS_ and self.Email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmail>%s</%sEmail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Email), input_name='Email')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Telefone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Telefone')
            value_ = self.gds_validate_string(value_, node, 'Telefone')
            self.Telefone = value_
            self.Telefone_nsprefix_ = child_.prefix
            # validate type tsTelefone
            self.validate_tsTelefone(self.Telefone)
        elif nodeName_ == 'Email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Email')
            value_ = self.gds_validate_string(value_, node, 'Email')
            self.Email = value_
            self.Email_nsprefix_ = child_.prefix
            # validate type tsEmail
            self.validate_tsEmail(self.Email)
# end class tcContato


class tcIdentificacaoOrgaoGerador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CodigoMunicipio', ['tsCodigoMunicipioIbge', 'xsd:int'], 0, 0, {'name': 'CodigoMunicipio', 'type': 'xsd:int'}, None),
        MemberSpec_('Uf', ['tsUf', 'xsd:string'], 0, 0, {'name': 'Uf', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CodigoMunicipio=None, Uf=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoMunicipio = CodigoMunicipio
        self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
        self.CodigoMunicipio_nsprefix_ = None
        self.Uf = Uf
        self.validate_tsUf(self.Uf)
        self.Uf_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoOrgaoGerador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoOrgaoGerador.subclass:
            return tcIdentificacaoOrgaoGerador.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoOrgaoGerador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCodigoMunicipioIbge(self, value):
        result = True
        # Validate type tsCodigoMunicipioIbge, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsCodigoMunicipioIbge' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsUf(self, value):
        result = True
        # Validate type tsUf, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsUf' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.CodigoMunicipio is not None or
            self.Uf is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoOrgaoGerador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoOrgaoGerador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoOrgaoGerador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoOrgaoGerador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoOrgaoGerador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoOrgaoGerador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoOrgaoGerador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoMunicipio is not None:
            namespaceprefix_ = self.CodigoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoMunicipio>%s</%sCodigoMunicipio>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoMunicipio, input_name='CodigoMunicipio'), namespaceprefix_ , eol_))
        if self.Uf is not None:
            namespaceprefix_ = self.Uf_nsprefix_ + ':' if (UseCapturedNS_ and self.Uf_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUf>%s</%sUf>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Uf), input_name='Uf')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoMunicipio' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoMunicipio')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoMunicipio')
            self.CodigoMunicipio = ival_
            self.CodigoMunicipio_nsprefix_ = child_.prefix
            # validate type tsCodigoMunicipioIbge
            self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
        elif nodeName_ == 'Uf':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Uf')
            value_ = self.gds_validate_string(value_, node, 'Uf')
            self.Uf = value_
            self.Uf_nsprefix_ = child_.prefix
            # validate type tsUf
            self.validate_tsUf(self.Uf)
# end class tcIdentificacaoOrgaoGerador


class tcIdentificacaoRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Numero', ['tsNumeroRps', 'xsd:nonNegativeInteger'], 0, 0, {'name': 'Numero', 'type': 'xsd:nonNegativeInteger'}, None),
        MemberSpec_('Serie', ['tsSerieRps', 'xsd:string'], 0, 0, {'name': 'Serie', 'type': 'xsd:string'}, None),
        MemberSpec_('Tipo', ['tsTipoRps', 'xsd:byte'], 0, 0, {'name': 'Tipo', 'type': 'xsd:byte'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Numero=None, Serie=None, Tipo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Numero = Numero
        self.validate_tsNumeroRps(self.Numero)
        self.Numero_nsprefix_ = None
        self.Serie = Serie
        self.validate_tsSerieRps(self.Serie)
        self.Serie_nsprefix_ = None
        self.Tipo = Tipo
        self.validate_tsTipoRps(self.Tipo)
        self.Tipo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoRps.subclass:
            return tcIdentificacaoRps.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsNumeroRps(self, value):
        result = True
        # Validate type tsNumeroRps, a restriction on xsd:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsNumeroRps' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsSerieRps(self, value):
        result = True
        # Validate type tsSerieRps, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsSerieRps' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsSerieRps' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsTipoRps(self, value):
        result = True
        # Validate type tsTipoRps, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsTipoRps_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsTipoRps_patterns_, ))
                result = False
        return result
    validate_tsTipoRps_patterns_ = [['^(1|2|3)$']]
    def hasContent_(self):
        if (
            self.Numero is not None or
            self.Serie is not None or
            self.Tipo is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoRps'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_format_integer(self.Numero, input_name='Numero'), namespaceprefix_ , eol_))
        if self.Serie is not None:
            namespaceprefix_ = self.Serie_nsprefix_ + ':' if (UseCapturedNS_ and self.Serie_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSerie>%s</%sSerie>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Serie), input_name='Serie')), namespaceprefix_ , eol_))
        if self.Tipo is not None:
            namespaceprefix_ = self.Tipo_nsprefix_ + ':' if (UseCapturedNS_ and self.Tipo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTipo>%s</%sTipo>%s' % (namespaceprefix_ , self.gds_format_integer(self.Tipo, input_name='Tipo'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Numero' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Numero')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'Numero')
            self.Numero = ival_
            self.Numero_nsprefix_ = child_.prefix
            # validate type tsNumeroRps
            self.validate_tsNumeroRps(self.Numero)
        elif nodeName_ == 'Serie':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Serie')
            value_ = self.gds_validate_string(value_, node, 'Serie')
            self.Serie = value_
            self.Serie_nsprefix_ = child_.prefix
            # validate type tsSerieRps
            self.validate_tsSerieRps(self.Serie)
        elif nodeName_ == 'Tipo' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Tipo')
            ival_ = self.gds_validate_integer(ival_, node, 'Tipo')
            self.Tipo = ival_
            self.Tipo_nsprefix_ = child_.prefix
            # validate type tsTipoRps
            self.validate_tsTipoRps(self.Tipo)
# end class tcIdentificacaoRps


class tcIdentificacaoPrestador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Cnpj', ['tsCnpj', 'xsd:string'], 0, 0, {'name': 'Cnpj', 'type': 'xsd:string'}, None),
        MemberSpec_('InscricaoMunicipal', ['tsInscricaoMunicipal', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'InscricaoMunicipal', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Cnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Cnpj = Cnpj
        self.validate_tsCnpj(self.Cnpj)
        self.Cnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoPrestador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoPrestador.subclass:
            return tcIdentificacaoPrestador.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoPrestador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCnpj(self, value):
        result = True
        # Validate type tsCnpj, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsCnpj' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsInscricaoMunicipal(self, value):
        result = True
        # Validate type tsInscricaoMunicipal, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Cnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoPrestador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoPrestador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoPrestador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoPrestador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoPrestador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoPrestador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoPrestador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cnpj is not None:
            namespaceprefix_ = self.Cnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnpj_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnpj>%s</%sCnpj>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cnpj), input_name='Cnpj')), namespaceprefix_ , eol_))
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Cnpj':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnpj')
            value_ = self.gds_validate_string(value_, node, 'Cnpj')
            self.Cnpj = value_
            self.Cnpj_nsprefix_ = child_.prefix
            # validate type tsCnpj
            self.validate_tsCnpj(self.Cnpj)
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
            # validate type tsInscricaoMunicipal
            self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
# end class tcIdentificacaoPrestador


class tcIdentificacaoTomador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CpfCnpj', 'tcCpfCnpj', 0, 1, {'minOccurs': '0', 'name': 'CpfCnpj', 'type': 'tcCpfCnpj'}, None),
        MemberSpec_('InscricaoMunicipal', ['tsInscricaoMunicipal', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'InscricaoMunicipal', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CpfCnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoTomador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoTomador.subclass:
            return tcIdentificacaoTomador.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoTomador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsInscricaoMunicipal(self, value):
        result = True
        # Validate type tsInscricaoMunicipal, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoTomador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoTomador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoTomador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoTomador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoTomador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoTomador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoTomador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
            # validate type tsInscricaoMunicipal
            self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
# end class tcIdentificacaoTomador


class tcDadosTomador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('IdentificacaoTomador', 'tcIdentificacaoTomador', 0, 1, {'minOccurs': '0', 'name': 'IdentificacaoTomador', 'type': 'tcIdentificacaoTomador'}, None),
        MemberSpec_('RazaoSocial', ['tsRazaoSocial', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'RazaoSocial', 'type': 'xsd:string'}, None),
        MemberSpec_('Endereco', 'tcEndereco', 0, 1, {'minOccurs': '0', 'name': 'Endereco', 'type': 'tcEndereco'}, None),
        MemberSpec_('Contato', 'tcContato', 0, 1, {'minOccurs': '0', 'name': 'Contato', 'type': 'tcContato'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoTomador=None, RazaoSocial=None, Endereco=None, Contato=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoTomador = IdentificacaoTomador
        self.IdentificacaoTomador_nsprefix_ = None
        self.RazaoSocial = RazaoSocial
        self.validate_tsRazaoSocial(self.RazaoSocial)
        self.RazaoSocial_nsprefix_ = None
        self.Endereco = Endereco
        self.Endereco_nsprefix_ = None
        self.Contato = Contato
        self.Contato_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosTomador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosTomador.subclass:
            return tcDadosTomador.subclass(*args_, **kwargs_)
        else:
            return tcDadosTomador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsRazaoSocial(self, value):
        result = True
        # Validate type tsRazaoSocial, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 115:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.IdentificacaoTomador is not None or
            self.RazaoSocial is not None or
            self.Endereco is not None or
            self.Contato is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosTomador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosTomador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosTomador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosTomador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosTomador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosTomador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosTomador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoTomador is not None:
            namespaceprefix_ = self.IdentificacaoTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoTomador_nsprefix_) else ''
            self.IdentificacaoTomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoTomador', pretty_print=pretty_print)
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.Endereco is not None:
            namespaceprefix_ = self.Endereco_nsprefix_ + ':' if (UseCapturedNS_ and self.Endereco_nsprefix_) else ''
            self.Endereco.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Endereco', pretty_print=pretty_print)
        if self.Contato is not None:
            namespaceprefix_ = self.Contato_nsprefix_ + ':' if (UseCapturedNS_ and self.Contato_nsprefix_) else ''
            self.Contato.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Contato', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoTomador':
            obj_ = tcIdentificacaoTomador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoTomador = obj_
            obj_.original_tagname_ = 'IdentificacaoTomador'
        elif nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
            # validate type tsRazaoSocial
            self.validate_tsRazaoSocial(self.RazaoSocial)
        elif nodeName_ == 'Endereco':
            obj_ = tcEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Endereco = obj_
            obj_.original_tagname_ = 'Endereco'
        elif nodeName_ == 'Contato':
            obj_ = tcContato.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Contato = obj_
            obj_.original_tagname_ = 'Contato'
# end class tcDadosTomador


class tcIdentificacaoIntermediarioServico(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('RazaoSocial', ['tsRazaoSocial', 'xsd:string'], 0, 0, {'name': 'RazaoSocial', 'type': 'xsd:string'}, None),
        MemberSpec_('CpfCnpj', 'tcCpfCnpj', 0, 0, {'name': 'CpfCnpj', 'type': 'tcCpfCnpj'}, None),
        MemberSpec_('InscricaoMunicipal', ['tsInscricaoMunicipal', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'InscricaoMunicipal', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, RazaoSocial=None, CpfCnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RazaoSocial = RazaoSocial
        self.validate_tsRazaoSocial(self.RazaoSocial)
        self.RazaoSocial_nsprefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoIntermediarioServico)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoIntermediarioServico.subclass:
            return tcIdentificacaoIntermediarioServico.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoIntermediarioServico(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsRazaoSocial(self, value):
        result = True
        # Validate type tsRazaoSocial, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 115:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsInscricaoMunicipal(self, value):
        result = True
        # Validate type tsInscricaoMunicipal, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.RazaoSocial is not None or
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoIntermediarioServico', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoIntermediarioServico')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoIntermediarioServico':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoIntermediarioServico')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoIntermediarioServico', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoIntermediarioServico'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoIntermediarioServico', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
            # validate type tsRazaoSocial
            self.validate_tsRazaoSocial(self.RazaoSocial)
        elif nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
            # validate type tsInscricaoMunicipal
            self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
# end class tcIdentificacaoIntermediarioServico


class tcValores(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('ValorServicos', ['tsValor', 'xsd:decimal'], 0, 0, {'name': 'ValorServicos', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorDeducoes', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorDeducoes', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorPis', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorPis', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorCofins', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorCofins', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorInss', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorInss', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorIr', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorIr', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorCsll', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorCsll', 'type': 'xsd:decimal'}, None),
        MemberSpec_('IssRetido', ['tsSimNao', 'xsd:byte'], 0, 0, {'name': 'IssRetido', 'type': 'xsd:byte'}, None),
        MemberSpec_('ValorIss', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorIss', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorIssRetido', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorIssRetido', 'type': 'xsd:decimal'}, None),
        MemberSpec_('OutrasRetencoes', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'OutrasRetencoes', 'type': 'xsd:decimal'}, None),
        MemberSpec_('BaseCalculo', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'BaseCalculo', 'type': 'xsd:decimal'}, None),
        MemberSpec_('Aliquota', ['tsAliquota', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'Aliquota', 'type': 'xsd:decimal'}, None),
        MemberSpec_('ValorLiquidoNfse', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorLiquidoNfse', 'type': 'xsd:decimal'}, None),
        MemberSpec_('DescontoIncondicionado', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'DescontoIncondicionado', 'type': 'xsd:decimal'}, None),
        MemberSpec_('DescontoCondicionado', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'DescontoCondicionado', 'type': 'xsd:decimal'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, ValorServicos=None, ValorDeducoes=None, ValorPis=None, ValorCofins=None, ValorInss=None, ValorIr=None, ValorCsll=None, IssRetido=None, ValorIss=None, ValorIssRetido=None, OutrasRetencoes=None, BaseCalculo=None, Aliquota=None, ValorLiquidoNfse=None, DescontoIncondicionado=None, DescontoCondicionado=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ValorServicos = ValorServicos
        self.validate_tsValor(self.ValorServicos)
        self.ValorServicos_nsprefix_ = None
        self.ValorDeducoes = ValorDeducoes
        self.validate_tsValor(self.ValorDeducoes)
        self.ValorDeducoes_nsprefix_ = None
        self.ValorPis = ValorPis
        self.validate_tsValor(self.ValorPis)
        self.ValorPis_nsprefix_ = None
        self.ValorCofins = ValorCofins
        self.validate_tsValor(self.ValorCofins)
        self.ValorCofins_nsprefix_ = None
        self.ValorInss = ValorInss
        self.validate_tsValor(self.ValorInss)
        self.ValorInss_nsprefix_ = None
        self.ValorIr = ValorIr
        self.validate_tsValor(self.ValorIr)
        self.ValorIr_nsprefix_ = None
        self.ValorCsll = ValorCsll
        self.validate_tsValor(self.ValorCsll)
        self.ValorCsll_nsprefix_ = None
        self.IssRetido = IssRetido
        self.validate_tsSimNao(self.IssRetido)
        self.IssRetido_nsprefix_ = None
        self.ValorIss = ValorIss
        self.validate_tsValor(self.ValorIss)
        self.ValorIss_nsprefix_ = None
        self.ValorIssRetido = ValorIssRetido
        self.validate_tsValor(self.ValorIssRetido)
        self.ValorIssRetido_nsprefix_ = None
        self.OutrasRetencoes = OutrasRetencoes
        self.validate_tsValor(self.OutrasRetencoes)
        self.OutrasRetencoes_nsprefix_ = None
        self.BaseCalculo = BaseCalculo
        self.validate_tsValor(self.BaseCalculo)
        self.BaseCalculo_nsprefix_ = None
        self.Aliquota = Aliquota
        self.validate_tsAliquota(self.Aliquota)
        self.Aliquota_nsprefix_ = None
        self.ValorLiquidoNfse = ValorLiquidoNfse
        self.validate_tsValor(self.ValorLiquidoNfse)
        self.ValorLiquidoNfse_nsprefix_ = None
        self.DescontoIncondicionado = DescontoIncondicionado
        self.validate_tsValor(self.DescontoIncondicionado)
        self.DescontoIncondicionado_nsprefix_ = None
        self.DescontoCondicionado = DescontoCondicionado
        self.validate_tsValor(self.DescontoCondicionado)
        self.DescontoCondicionado_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcValores)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcValores.subclass:
            return tcValores.subclass(*args_, **kwargs_)
        else:
            return tcValores(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsValor(self, value):
        result = True
        # Validate type tsValor, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tsValor' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsValor' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsSimNao(self, value):
        result = True
        # Validate type tsSimNao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsSimNao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsSimNao_patterns_, ))
                result = False
        return result
    validate_tsSimNao_patterns_ = [['^(1|2)$']]
    def validate_tsAliquota(self, value):
        result = True
        # Validate type tsAliquota, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tsAliquota' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsAliquota' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.ValorServicos is not None or
            self.ValorDeducoes is not None or
            self.ValorPis is not None or
            self.ValorCofins is not None or
            self.ValorInss is not None or
            self.ValorIr is not None or
            self.ValorCsll is not None or
            self.IssRetido is not None or
            self.ValorIss is not None or
            self.ValorIssRetido is not None or
            self.OutrasRetencoes is not None or
            self.BaseCalculo is not None or
            self.Aliquota is not None or
            self.ValorLiquidoNfse is not None or
            self.DescontoIncondicionado is not None or
            self.DescontoCondicionado is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcValores', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcValores')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcValores':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcValores')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcValores', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcValores'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcValores', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ValorServicos is not None:
            namespaceprefix_ = self.ValorServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorServicos>%s</%sValorServicos>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorServicos, input_name='ValorServicos'), namespaceprefix_ , eol_))
        if self.ValorDeducoes is not None:
            namespaceprefix_ = self.ValorDeducoes_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDeducoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDeducoes>%s</%sValorDeducoes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorDeducoes, input_name='ValorDeducoes'), namespaceprefix_ , eol_))
        if self.ValorPis is not None:
            namespaceprefix_ = self.ValorPis_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPis>%s</%sValorPis>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPis, input_name='ValorPis'), namespaceprefix_ , eol_))
        if self.ValorCofins is not None:
            namespaceprefix_ = self.ValorCofins_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCofins_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCofins>%s</%sValorCofins>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCofins, input_name='ValorCofins'), namespaceprefix_ , eol_))
        if self.ValorInss is not None:
            namespaceprefix_ = self.ValorInss_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorInss_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorInss>%s</%sValorInss>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorInss, input_name='ValorInss'), namespaceprefix_ , eol_))
        if self.ValorIr is not None:
            namespaceprefix_ = self.ValorIr_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIr_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIr>%s</%sValorIr>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIr, input_name='ValorIr'), namespaceprefix_ , eol_))
        if self.ValorCsll is not None:
            namespaceprefix_ = self.ValorCsll_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCsll_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCsll>%s</%sValorCsll>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCsll, input_name='ValorCsll'), namespaceprefix_ , eol_))
        if self.IssRetido is not None:
            namespaceprefix_ = self.IssRetido_nsprefix_ + ':' if (UseCapturedNS_ and self.IssRetido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIssRetido>%s</%sIssRetido>%s' % (namespaceprefix_ , self.gds_format_integer(self.IssRetido, input_name='IssRetido'), namespaceprefix_ , eol_))
        if self.ValorIss is not None:
            namespaceprefix_ = self.ValorIss_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIss_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIss>%s</%sValorIss>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIss, input_name='ValorIss'), namespaceprefix_ , eol_))
        if self.ValorIssRetido is not None:
            namespaceprefix_ = self.ValorIssRetido_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIssRetido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIssRetido>%s</%sValorIssRetido>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIssRetido, input_name='ValorIssRetido'), namespaceprefix_ , eol_))
        if self.OutrasRetencoes is not None:
            namespaceprefix_ = self.OutrasRetencoes_nsprefix_ + ':' if (UseCapturedNS_ and self.OutrasRetencoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOutrasRetencoes>%s</%sOutrasRetencoes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.OutrasRetencoes, input_name='OutrasRetencoes'), namespaceprefix_ , eol_))
        if self.BaseCalculo is not None:
            namespaceprefix_ = self.BaseCalculo_nsprefix_ + ':' if (UseCapturedNS_ and self.BaseCalculo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBaseCalculo>%s</%sBaseCalculo>%s' % (namespaceprefix_ , self.gds_format_decimal(self.BaseCalculo, input_name='BaseCalculo'), namespaceprefix_ , eol_))
        if self.Aliquota is not None:
            namespaceprefix_ = self.Aliquota_nsprefix_ + ':' if (UseCapturedNS_ and self.Aliquota_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAliquota>%s</%sAliquota>%s' % (namespaceprefix_ , self.gds_format_decimal(self.Aliquota, input_name='Aliquota'), namespaceprefix_ , eol_))
        if self.ValorLiquidoNfse is not None:
            namespaceprefix_ = self.ValorLiquidoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorLiquidoNfse_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorLiquidoNfse>%s</%sValorLiquidoNfse>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorLiquidoNfse, input_name='ValorLiquidoNfse'), namespaceprefix_ , eol_))
        if self.DescontoIncondicionado is not None:
            namespaceprefix_ = self.DescontoIncondicionado_nsprefix_ + ':' if (UseCapturedNS_ and self.DescontoIncondicionado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescontoIncondicionado>%s</%sDescontoIncondicionado>%s' % (namespaceprefix_ , self.gds_format_decimal(self.DescontoIncondicionado, input_name='DescontoIncondicionado'), namespaceprefix_ , eol_))
        if self.DescontoCondicionado is not None:
            namespaceprefix_ = self.DescontoCondicionado_nsprefix_ + ':' if (UseCapturedNS_ and self.DescontoCondicionado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescontoCondicionado>%s</%sDescontoCondicionado>%s' % (namespaceprefix_ , self.gds_format_decimal(self.DescontoCondicionado, input_name='DescontoCondicionado'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ValorServicos' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorServicos')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorServicos')
            self.ValorServicos = fval_
            self.ValorServicos_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorServicos)
        elif nodeName_ == 'ValorDeducoes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorDeducoes')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorDeducoes')
            self.ValorDeducoes = fval_
            self.ValorDeducoes_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorDeducoes)
        elif nodeName_ == 'ValorPis' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPis')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPis')
            self.ValorPis = fval_
            self.ValorPis_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorPis)
        elif nodeName_ == 'ValorCofins' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCofins')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCofins')
            self.ValorCofins = fval_
            self.ValorCofins_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorCofins)
        elif nodeName_ == 'ValorInss' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorInss')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorInss')
            self.ValorInss = fval_
            self.ValorInss_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorInss)
        elif nodeName_ == 'ValorIr' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIr')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIr')
            self.ValorIr = fval_
            self.ValorIr_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorIr)
        elif nodeName_ == 'ValorCsll' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCsll')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCsll')
            self.ValorCsll = fval_
            self.ValorCsll_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorCsll)
        elif nodeName_ == 'IssRetido' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'IssRetido')
            ival_ = self.gds_validate_integer(ival_, node, 'IssRetido')
            self.IssRetido = ival_
            self.IssRetido_nsprefix_ = child_.prefix
            # validate type tsSimNao
            self.validate_tsSimNao(self.IssRetido)
        elif nodeName_ == 'ValorIss' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIss')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIss')
            self.ValorIss = fval_
            self.ValorIss_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorIss)
        elif nodeName_ == 'ValorIssRetido' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIssRetido')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIssRetido')
            self.ValorIssRetido = fval_
            self.ValorIssRetido_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorIssRetido)
        elif nodeName_ == 'OutrasRetencoes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'OutrasRetencoes')
            fval_ = self.gds_validate_decimal(fval_, node, 'OutrasRetencoes')
            self.OutrasRetencoes = fval_
            self.OutrasRetencoes_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.OutrasRetencoes)
        elif nodeName_ == 'BaseCalculo' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'BaseCalculo')
            fval_ = self.gds_validate_decimal(fval_, node, 'BaseCalculo')
            self.BaseCalculo = fval_
            self.BaseCalculo_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.BaseCalculo)
        elif nodeName_ == 'Aliquota' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'Aliquota')
            fval_ = self.gds_validate_decimal(fval_, node, 'Aliquota')
            self.Aliquota = fval_
            self.Aliquota_nsprefix_ = child_.prefix
            # validate type tsAliquota
            self.validate_tsAliquota(self.Aliquota)
        elif nodeName_ == 'ValorLiquidoNfse' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorLiquidoNfse')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorLiquidoNfse')
            self.ValorLiquidoNfse = fval_
            self.ValorLiquidoNfse_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorLiquidoNfse)
        elif nodeName_ == 'DescontoIncondicionado' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'DescontoIncondicionado')
            fval_ = self.gds_validate_decimal(fval_, node, 'DescontoIncondicionado')
            self.DescontoIncondicionado = fval_
            self.DescontoIncondicionado_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.DescontoIncondicionado)
        elif nodeName_ == 'DescontoCondicionado' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'DescontoCondicionado')
            fval_ = self.gds_validate_decimal(fval_, node, 'DescontoCondicionado')
            self.DescontoCondicionado = fval_
            self.DescontoCondicionado_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.DescontoCondicionado)
# end class tcValores


class tcDadosServico(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Valores', 'tcValores', 0, 0, {'name': 'Valores', 'type': 'tcValores'}, None),
        MemberSpec_('ItemListaServico', ['tsItemListaServico', 'xsd:string'], 0, 0, {'name': 'ItemListaServico', 'type': 'xsd:string'}, None),
        MemberSpec_('CodigoCnae', ['tsCodigoCnae', 'xsd:int'], 0, 1, {'minOccurs': '0', 'name': 'CodigoCnae', 'type': 'xsd:int'}, None),
        MemberSpec_('CodigoTributacaoMunicipio', ['tsCodigoTributacao', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'CodigoTributacaoMunicipio', 'type': 'xsd:string'}, None),
        MemberSpec_('Discriminacao', ['tsDiscriminacao', 'xsd:string'], 0, 0, {'name': 'Discriminacao', 'type': 'xsd:string'}, None),
        MemberSpec_('CodigoMunicipio', ['tsCodigoMunicipioIbge', 'xsd:int'], 0, 0, {'name': 'CodigoMunicipio', 'type': 'xsd:int'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Valores=None, ItemListaServico=None, CodigoCnae=None, CodigoTributacaoMunicipio=None, Discriminacao=None, CodigoMunicipio=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Valores = Valores
        self.Valores_nsprefix_ = None
        self.ItemListaServico = ItemListaServico
        self.validate_tsItemListaServico(self.ItemListaServico)
        self.ItemListaServico_nsprefix_ = None
        self.CodigoCnae = CodigoCnae
        self.validate_tsCodigoCnae(self.CodigoCnae)
        self.CodigoCnae_nsprefix_ = None
        self.CodigoTributacaoMunicipio = CodigoTributacaoMunicipio
        self.validate_tsCodigoTributacao(self.CodigoTributacaoMunicipio)
        self.CodigoTributacaoMunicipio_nsprefix_ = None
        self.Discriminacao = Discriminacao
        self.validate_tsDiscriminacao(self.Discriminacao)
        self.Discriminacao_nsprefix_ = None
        self.CodigoMunicipio = CodigoMunicipio
        self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
        self.CodigoMunicipio_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosServico)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosServico.subclass:
            return tcDadosServico.subclass(*args_, **kwargs_)
        else:
            return tcDadosServico(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsItemListaServico(self, value):
        result = True
        # Validate type tsItemListaServico, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsItemListaServico' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsItemListaServico' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsCodigoCnae(self, value):
        result = True
        # Validate type tsCodigoCnae, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsCodigoCnae' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsCodigoTributacao(self, value):
        result = True
        # Validate type tsCodigoTributacao, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsCodigoTributacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsCodigoTributacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsDiscriminacao(self, value):
        result = True
        # Validate type tsDiscriminacao, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsDiscriminacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsDiscriminacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsCodigoMunicipioIbge(self, value):
        result = True
        # Validate type tsCodigoMunicipioIbge, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsCodigoMunicipioIbge' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Valores is not None or
            self.ItemListaServico is not None or
            self.CodigoCnae is not None or
            self.CodigoTributacaoMunicipio is not None or
            self.Discriminacao is not None or
            self.CodigoMunicipio is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosServico', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosServico')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosServico':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosServico')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosServico', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosServico'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosServico', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Valores is not None:
            namespaceprefix_ = self.Valores_nsprefix_ + ':' if (UseCapturedNS_ and self.Valores_nsprefix_) else ''
            self.Valores.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Valores', pretty_print=pretty_print)
        if self.ItemListaServico is not None:
            namespaceprefix_ = self.ItemListaServico_nsprefix_ + ':' if (UseCapturedNS_ and self.ItemListaServico_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sItemListaServico>%s</%sItemListaServico>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ItemListaServico), input_name='ItemListaServico')), namespaceprefix_ , eol_))
        if self.CodigoCnae is not None:
            namespaceprefix_ = self.CodigoCnae_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCnae_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCnae>%s</%sCodigoCnae>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoCnae, input_name='CodigoCnae'), namespaceprefix_ , eol_))
        if self.CodigoTributacaoMunicipio is not None:
            namespaceprefix_ = self.CodigoTributacaoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoTributacaoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoTributacaoMunicipio>%s</%sCodigoTributacaoMunicipio>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoTributacaoMunicipio), input_name='CodigoTributacaoMunicipio')), namespaceprefix_ , eol_))
        if self.Discriminacao is not None:
            namespaceprefix_ = self.Discriminacao_nsprefix_ + ':' if (UseCapturedNS_ and self.Discriminacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDiscriminacao>%s</%sDiscriminacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Discriminacao), input_name='Discriminacao')), namespaceprefix_ , eol_))
        if self.CodigoMunicipio is not None:
            namespaceprefix_ = self.CodigoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoMunicipio>%s</%sCodigoMunicipio>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoMunicipio, input_name='CodigoMunicipio'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Valores':
            obj_ = tcValores.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Valores = obj_
            obj_.original_tagname_ = 'Valores'
        elif nodeName_ == 'ItemListaServico':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ItemListaServico')
            value_ = self.gds_validate_string(value_, node, 'ItemListaServico')
            self.ItemListaServico = value_
            self.ItemListaServico_nsprefix_ = child_.prefix
            # validate type tsItemListaServico
            self.validate_tsItemListaServico(self.ItemListaServico)
        elif nodeName_ == 'CodigoCnae' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoCnae')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoCnae')
            self.CodigoCnae = ival_
            self.CodigoCnae_nsprefix_ = child_.prefix
            # validate type tsCodigoCnae
            self.validate_tsCodigoCnae(self.CodigoCnae)
        elif nodeName_ == 'CodigoTributacaoMunicipio':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoTributacaoMunicipio')
            value_ = self.gds_validate_string(value_, node, 'CodigoTributacaoMunicipio')
            self.CodigoTributacaoMunicipio = value_
            self.CodigoTributacaoMunicipio_nsprefix_ = child_.prefix
            # validate type tsCodigoTributacao
            self.validate_tsCodigoTributacao(self.CodigoTributacaoMunicipio)
        elif nodeName_ == 'Discriminacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Discriminacao')
            value_ = self.gds_validate_string(value_, node, 'Discriminacao')
            self.Discriminacao = value_
            self.Discriminacao_nsprefix_ = child_.prefix
            # validate type tsDiscriminacao
            self.validate_tsDiscriminacao(self.Discriminacao)
        elif nodeName_ == 'CodigoMunicipio' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoMunicipio')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoMunicipio')
            self.CodigoMunicipio = ival_
            self.CodigoMunicipio_nsprefix_ = child_.prefix
            # validate type tsCodigoMunicipioIbge
            self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
# end class tcDadosServico


class tcDadosConstrucaoCivil(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CodigoObra', ['tsCodigoObra', 'xsd:string'], 0, 0, {'name': 'CodigoObra', 'type': 'xsd:string'}, None),
        MemberSpec_('Art', ['tsArt', 'xsd:string'], 0, 0, {'name': 'Art', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CodigoObra=None, Art=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoObra = CodigoObra
        self.validate_tsCodigoObra(self.CodigoObra)
        self.CodigoObra_nsprefix_ = None
        self.Art = Art
        self.validate_tsArt(self.Art)
        self.Art_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosConstrucaoCivil)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosConstrucaoCivil.subclass:
            return tcDadosConstrucaoCivil.subclass(*args_, **kwargs_)
        else:
            return tcDadosConstrucaoCivil(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCodigoObra(self, value):
        result = True
        # Validate type tsCodigoObra, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsCodigoObra' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsCodigoObra' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsArt(self, value):
        result = True
        # Validate type tsArt, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsArt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsArt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.CodigoObra is not None or
            self.Art is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosConstrucaoCivil', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosConstrucaoCivil')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosConstrucaoCivil':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosConstrucaoCivil')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosConstrucaoCivil', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosConstrucaoCivil'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosConstrucaoCivil', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoObra is not None:
            namespaceprefix_ = self.CodigoObra_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoObra_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoObra>%s</%sCodigoObra>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoObra), input_name='CodigoObra')), namespaceprefix_ , eol_))
        if self.Art is not None:
            namespaceprefix_ = self.Art_nsprefix_ + ':' if (UseCapturedNS_ and self.Art_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sArt>%s</%sArt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Art), input_name='Art')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoObra':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoObra')
            value_ = self.gds_validate_string(value_, node, 'CodigoObra')
            self.CodigoObra = value_
            self.CodigoObra_nsprefix_ = child_.prefix
            # validate type tsCodigoObra
            self.validate_tsCodigoObra(self.CodigoObra)
        elif nodeName_ == 'Art':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Art')
            value_ = self.gds_validate_string(value_, node, 'Art')
            self.Art = value_
            self.Art_nsprefix_ = child_.prefix
            # validate type tsArt
            self.validate_tsArt(self.Art)
# end class tcDadosConstrucaoCivil


class tcDadosPrestador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('IdentificacaoPrestador', 'tcIdentificacaoPrestador', 0, 0, {'name': 'IdentificacaoPrestador', 'type': 'tcIdentificacaoPrestador'}, None),
        MemberSpec_('RazaoSocial', ['tsRazaoSocial', 'xsd:string'], 0, 0, {'name': 'RazaoSocial', 'type': 'xsd:string'}, None),
        MemberSpec_('NomeFantasia', ['tsNomeFantasia', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'NomeFantasia', 'type': 'xsd:string'}, None),
        MemberSpec_('Endereco', 'tcEndereco', 0, 0, {'name': 'Endereco', 'type': 'tcEndereco'}, None),
        MemberSpec_('Contato', 'tcContato', 0, 1, {'minOccurs': '0', 'name': 'Contato', 'type': 'tcContato'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoPrestador=None, RazaoSocial=None, NomeFantasia=None, Endereco=None, Contato=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoPrestador = IdentificacaoPrestador
        self.IdentificacaoPrestador_nsprefix_ = None
        self.RazaoSocial = RazaoSocial
        self.validate_tsRazaoSocial(self.RazaoSocial)
        self.RazaoSocial_nsprefix_ = None
        self.NomeFantasia = NomeFantasia
        self.validate_tsNomeFantasia(self.NomeFantasia)
        self.NomeFantasia_nsprefix_ = None
        self.Endereco = Endereco
        self.Endereco_nsprefix_ = None
        self.Contato = Contato
        self.Contato_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosPrestador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosPrestador.subclass:
            return tcDadosPrestador.subclass(*args_, **kwargs_)
        else:
            return tcDadosPrestador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsRazaoSocial(self, value):
        result = True
        # Validate type tsRazaoSocial, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 115:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsNomeFantasia(self, value):
        result = True
        # Validate type tsNomeFantasia, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsNomeFantasia' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsNomeFantasia' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.IdentificacaoPrestador is not None or
            self.RazaoSocial is not None or
            self.NomeFantasia is not None or
            self.Endereco is not None or
            self.Contato is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosPrestador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosPrestador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosPrestador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosPrestador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosPrestador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosPrestador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcDadosPrestador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoPrestador is not None:
            namespaceprefix_ = self.IdentificacaoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoPrestador_nsprefix_) else ''
            self.IdentificacaoPrestador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoPrestador', pretty_print=pretty_print)
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.NomeFantasia is not None:
            namespaceprefix_ = self.NomeFantasia_nsprefix_ + ':' if (UseCapturedNS_ and self.NomeFantasia_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNomeFantasia>%s</%sNomeFantasia>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NomeFantasia), input_name='NomeFantasia')), namespaceprefix_ , eol_))
        if self.Endereco is not None:
            namespaceprefix_ = self.Endereco_nsprefix_ + ':' if (UseCapturedNS_ and self.Endereco_nsprefix_) else ''
            self.Endereco.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Endereco', pretty_print=pretty_print)
        if self.Contato is not None:
            namespaceprefix_ = self.Contato_nsprefix_ + ':' if (UseCapturedNS_ and self.Contato_nsprefix_) else ''
            self.Contato.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Contato', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoPrestador':
            obj_ = tcIdentificacaoPrestador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoPrestador = obj_
            obj_.original_tagname_ = 'IdentificacaoPrestador'
        elif nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
            # validate type tsRazaoSocial
            self.validate_tsRazaoSocial(self.RazaoSocial)
        elif nodeName_ == 'NomeFantasia':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NomeFantasia')
            value_ = self.gds_validate_string(value_, node, 'NomeFantasia')
            self.NomeFantasia = value_
            self.NomeFantasia_nsprefix_ = child_.prefix
            # validate type tsNomeFantasia
            self.validate_tsNomeFantasia(self.NomeFantasia)
        elif nodeName_ == 'Endereco':
            obj_ = tcEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Endereco = obj_
            obj_.original_tagname_ = 'Endereco'
        elif nodeName_ == 'Contato':
            obj_ = tcContato.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Contato = obj_
            obj_.original_tagname_ = 'Contato'
# end class tcDadosPrestador


class tcInfRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'tsIdTag', 0, 1, {'use': 'optional'}),
        MemberSpec_('IdentificacaoRps', 'tcIdentificacaoRps', 0, 0, {'name': 'IdentificacaoRps', 'type': 'tcIdentificacaoRps'}, None),
        MemberSpec_('DataEmissao', 'xsd:dateTime', 0, 0, {'name': 'DataEmissao', 'type': 'xsd:dateTime'}, None),
        MemberSpec_('NaturezaOperacao', ['tsNaturezaOperacao', 'xsd:byte'], 0, 0, {'name': 'NaturezaOperacao', 'type': 'xsd:byte'}, None),
        MemberSpec_('RegimeEspecialTributacao', ['tsRegimeEspecialTributacao', 'xsd:byte'], 0, 1, {'minOccurs': '0', 'name': 'RegimeEspecialTributacao', 'type': 'xsd:byte'}, None),
        MemberSpec_('OptanteSimplesNacional', ['tsSimNao', 'xsd:byte'], 0, 0, {'name': 'OptanteSimplesNacional', 'type': 'xsd:byte'}, None),
        MemberSpec_('IncentivadorCultural', ['tsSimNao', 'xsd:byte'], 0, 0, {'name': 'IncentivadorCultural', 'type': 'xsd:byte'}, None),
        MemberSpec_('Status', ['tsStatusRps', 'xsd:byte'], 0, 0, {'name': 'Status', 'type': 'xsd:byte'}, None),
        MemberSpec_('RpsSubstituido', 'tcIdentificacaoRps', 0, 1, {'minOccurs': '0', 'name': 'RpsSubstituido', 'type': 'tcIdentificacaoRps'}, None),
        MemberSpec_('Servico', 'tcDadosServico', 0, 0, {'name': 'Servico', 'type': 'tcDadosServico'}, None),
        MemberSpec_('Prestador', 'tcIdentificacaoPrestador', 0, 0, {'name': 'Prestador', 'type': 'tcIdentificacaoPrestador'}, None),
        MemberSpec_('Tomador', 'tcDadosTomador', 0, 0, {'name': 'Tomador', 'type': 'tcDadosTomador'}, None),
        MemberSpec_('IntermediarioServico', 'tcIdentificacaoIntermediarioServico', 0, 1, {'minOccurs': '0', 'name': 'IntermediarioServico', 'type': 'tcIdentificacaoIntermediarioServico'}, None),
        MemberSpec_('ConstrucaoCivil', 'tcDadosConstrucaoCivil', 0, 1, {'minOccurs': '0', 'name': 'ConstrucaoCivil', 'type': 'tcDadosConstrucaoCivil'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, IdentificacaoRps=None, DataEmissao=None, NaturezaOperacao=None, RegimeEspecialTributacao=None, OptanteSimplesNacional=None, IncentivadorCultural=None, Status=None, RpsSubstituido=None, Servico=None, Prestador=None, Tomador=None, IntermediarioServico=None, ConstrucaoCivil=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.IdentificacaoRps = IdentificacaoRps
        self.IdentificacaoRps_nsprefix_ = None
        if isinstance(DataEmissao, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissao, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEmissao
        self.DataEmissao = initvalue_
        self.DataEmissao_nsprefix_ = None
        self.NaturezaOperacao = NaturezaOperacao
        self.validate_tsNaturezaOperacao(self.NaturezaOperacao)
        self.NaturezaOperacao_nsprefix_ = None
        self.RegimeEspecialTributacao = RegimeEspecialTributacao
        self.validate_tsRegimeEspecialTributacao(self.RegimeEspecialTributacao)
        self.RegimeEspecialTributacao_nsprefix_ = None
        self.OptanteSimplesNacional = OptanteSimplesNacional
        self.validate_tsSimNao(self.OptanteSimplesNacional)
        self.OptanteSimplesNacional_nsprefix_ = None
        self.IncentivadorCultural = IncentivadorCultural
        self.validate_tsSimNao(self.IncentivadorCultural)
        self.IncentivadorCultural_nsprefix_ = None
        self.Status = Status
        self.validate_tsStatusRps(self.Status)
        self.Status_nsprefix_ = None
        self.RpsSubstituido = RpsSubstituido
        self.RpsSubstituido_nsprefix_ = None
        self.Servico = Servico
        self.Servico_nsprefix_ = None
        self.Prestador = Prestador
        self.Prestador_nsprefix_ = None
        self.Tomador = Tomador
        self.Tomador_nsprefix_ = None
        self.IntermediarioServico = IntermediarioServico
        self.IntermediarioServico_nsprefix_ = None
        self.ConstrucaoCivil = ConstrucaoCivil
        self.ConstrucaoCivil_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfRps.subclass:
            return tcInfRps.subclass(*args_, **kwargs_)
        else:
            return tcInfRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsNaturezaOperacao(self, value):
        result = True
        # Validate type tsNaturezaOperacao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsNaturezaOperacao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsNaturezaOperacao_patterns_, ))
                result = False
        return result
    validate_tsNaturezaOperacao_patterns_ = [['^(1|2|3|4|5|6)$']]
    def validate_tsRegimeEspecialTributacao(self, value):
        result = True
        # Validate type tsRegimeEspecialTributacao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsRegimeEspecialTributacao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsRegimeEspecialTributacao_patterns_, ))
                result = False
        return result
    validate_tsRegimeEspecialTributacao_patterns_ = [['^(0|1|2|3|4|5|6)$']]
    def validate_tsSimNao(self, value):
        result = True
        # Validate type tsSimNao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsSimNao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsSimNao_patterns_, ))
                result = False
        return result
    validate_tsSimNao_patterns_ = [['^(1|2)$']]
    def validate_tsStatusRps(self, value):
        result = True
        # Validate type tsStatusRps, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsStatusRps_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsStatusRps_patterns_, ))
                result = False
        return result
    validate_tsStatusRps_patterns_ = [['^(1|2)$']]
    def validate_tsIdTag(self, value):
        # Validate type tsIdTag, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsIdTag' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.IdentificacaoRps is not None or
            self.DataEmissao is not None or
            self.NaturezaOperacao is not None or
            self.RegimeEspecialTributacao is not None or
            self.OptanteSimplesNacional is not None or
            self.IncentivadorCultural is not None or
            self.Status is not None or
            self.RpsSubstituido is not None or
            self.Servico is not None or
            self.Prestador is not None or
            self.Tomador is not None or
            self.IntermediarioServico is not None or
            self.ConstrucaoCivil is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfRps'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoRps is not None:
            namespaceprefix_ = self.IdentificacaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoRps_nsprefix_) else ''
            self.IdentificacaoRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoRps', pretty_print=pretty_print)
        if self.DataEmissao is not None:
            namespaceprefix_ = self.DataEmissao_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissao>%s</%sDataEmissao>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEmissao, input_name='DataEmissao'), namespaceprefix_ , eol_))
        if self.NaturezaOperacao is not None:
            namespaceprefix_ = self.NaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.NaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaturezaOperacao>%s</%sNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.NaturezaOperacao, input_name='NaturezaOperacao'), namespaceprefix_ , eol_))
        if self.RegimeEspecialTributacao is not None:
            namespaceprefix_ = self.RegimeEspecialTributacao_nsprefix_ + ':' if (UseCapturedNS_ and self.RegimeEspecialTributacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRegimeEspecialTributacao>%s</%sRegimeEspecialTributacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.RegimeEspecialTributacao, input_name='RegimeEspecialTributacao'), namespaceprefix_ , eol_))
        if self.OptanteSimplesNacional is not None:
            namespaceprefix_ = self.OptanteSimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.OptanteSimplesNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOptanteSimplesNacional>%s</%sOptanteSimplesNacional>%s' % (namespaceprefix_ , self.gds_format_integer(self.OptanteSimplesNacional, input_name='OptanteSimplesNacional'), namespaceprefix_ , eol_))
        if self.IncentivadorCultural is not None:
            namespaceprefix_ = self.IncentivadorCultural_nsprefix_ + ':' if (UseCapturedNS_ and self.IncentivadorCultural_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIncentivadorCultural>%s</%sIncentivadorCultural>%s' % (namespaceprefix_ , self.gds_format_integer(self.IncentivadorCultural, input_name='IncentivadorCultural'), namespaceprefix_ , eol_))
        if self.Status is not None:
            namespaceprefix_ = self.Status_nsprefix_ + ':' if (UseCapturedNS_ and self.Status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatus>%s</%sStatus>%s' % (namespaceprefix_ , self.gds_format_integer(self.Status, input_name='Status'), namespaceprefix_ , eol_))
        if self.RpsSubstituido is not None:
            namespaceprefix_ = self.RpsSubstituido_nsprefix_ + ':' if (UseCapturedNS_ and self.RpsSubstituido_nsprefix_) else ''
            self.RpsSubstituido.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RpsSubstituido', pretty_print=pretty_print)
        if self.Servico is not None:
            namespaceprefix_ = self.Servico_nsprefix_ + ':' if (UseCapturedNS_ and self.Servico_nsprefix_) else ''
            self.Servico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Servico', pretty_print=pretty_print)
        if self.Prestador is not None:
            namespaceprefix_ = self.Prestador_nsprefix_ + ':' if (UseCapturedNS_ and self.Prestador_nsprefix_) else ''
            self.Prestador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Prestador', pretty_print=pretty_print)
        if self.Tomador is not None:
            namespaceprefix_ = self.Tomador_nsprefix_ + ':' if (UseCapturedNS_ and self.Tomador_nsprefix_) else ''
            self.Tomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Tomador', pretty_print=pretty_print)
        if self.IntermediarioServico is not None:
            namespaceprefix_ = self.IntermediarioServico_nsprefix_ + ':' if (UseCapturedNS_ and self.IntermediarioServico_nsprefix_) else ''
            self.IntermediarioServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IntermediarioServico', pretty_print=pretty_print)
        if self.ConstrucaoCivil is not None:
            namespaceprefix_ = self.ConstrucaoCivil_nsprefix_ + ':' if (UseCapturedNS_ and self.ConstrucaoCivil_nsprefix_) else ''
            self.ConstrucaoCivil.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ConstrucaoCivil', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_tsIdTag(self.Id)    # validate type tsIdTag
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoRps':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoRps = obj_
            obj_.original_tagname_ = 'IdentificacaoRps'
        elif nodeName_ == 'DataEmissao':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEmissao = dval_
            self.DataEmissao_nsprefix_ = child_.prefix
        elif nodeName_ == 'NaturezaOperacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NaturezaOperacao')
            ival_ = self.gds_validate_integer(ival_, node, 'NaturezaOperacao')
            self.NaturezaOperacao = ival_
            self.NaturezaOperacao_nsprefix_ = child_.prefix
            # validate type tsNaturezaOperacao
            self.validate_tsNaturezaOperacao(self.NaturezaOperacao)
        elif nodeName_ == 'RegimeEspecialTributacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'RegimeEspecialTributacao')
            ival_ = self.gds_validate_integer(ival_, node, 'RegimeEspecialTributacao')
            self.RegimeEspecialTributacao = ival_
            self.RegimeEspecialTributacao_nsprefix_ = child_.prefix
            # validate type tsRegimeEspecialTributacao
            self.validate_tsRegimeEspecialTributacao(self.RegimeEspecialTributacao)
        elif nodeName_ == 'OptanteSimplesNacional' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'OptanteSimplesNacional')
            ival_ = self.gds_validate_integer(ival_, node, 'OptanteSimplesNacional')
            self.OptanteSimplesNacional = ival_
            self.OptanteSimplesNacional_nsprefix_ = child_.prefix
            # validate type tsSimNao
            self.validate_tsSimNao(self.OptanteSimplesNacional)
        elif nodeName_ == 'IncentivadorCultural' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'IncentivadorCultural')
            ival_ = self.gds_validate_integer(ival_, node, 'IncentivadorCultural')
            self.IncentivadorCultural = ival_
            self.IncentivadorCultural_nsprefix_ = child_.prefix
            # validate type tsSimNao
            self.validate_tsSimNao(self.IncentivadorCultural)
        elif nodeName_ == 'Status' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Status')
            ival_ = self.gds_validate_integer(ival_, node, 'Status')
            self.Status = ival_
            self.Status_nsprefix_ = child_.prefix
            # validate type tsStatusRps
            self.validate_tsStatusRps(self.Status)
        elif nodeName_ == 'RpsSubstituido':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RpsSubstituido = obj_
            obj_.original_tagname_ = 'RpsSubstituido'
        elif nodeName_ == 'Servico':
            obj_ = tcDadosServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Servico = obj_
            obj_.original_tagname_ = 'Servico'
        elif nodeName_ == 'Prestador':
            obj_ = tcIdentificacaoPrestador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Prestador = obj_
            obj_.original_tagname_ = 'Prestador'
        elif nodeName_ == 'Tomador':
            obj_ = tcDadosTomador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Tomador = obj_
            obj_.original_tagname_ = 'Tomador'
        elif nodeName_ == 'IntermediarioServico':
            obj_ = tcIdentificacaoIntermediarioServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IntermediarioServico = obj_
            obj_.original_tagname_ = 'IntermediarioServico'
        elif nodeName_ == 'ConstrucaoCivil':
            obj_ = tcDadosConstrucaoCivil.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ConstrucaoCivil = obj_
            obj_.original_tagname_ = 'ConstrucaoCivil'
# end class tcInfRps


class tcRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('InfRps', 'tcInfRps', 0, 0, {'name': 'InfRps', 'type': 'tcInfRps'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, InfRps=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InfRps = InfRps
        self.InfRps_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcRps.subclass:
            return tcRps.subclass(*args_, **kwargs_)
        else:
            return tcRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.InfRps is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcRps'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InfRps is not None:
            namespaceprefix_ = self.InfRps_nsprefix_ + ':' if (UseCapturedNS_ and self.InfRps_nsprefix_) else ''
            self.InfRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfRps', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='dsig:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InfRps':
            obj_ = tcInfRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfRps = obj_
            obj_.original_tagname_ = 'InfRps'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class tcRps


class tcIdentificacaoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Numero', ['tsNumeroNfse', 'xsd:nonNegativeInteger'], 0, 0, {'name': 'Numero', 'type': 'xsd:nonNegativeInteger'}, None),
        MemberSpec_('Cnpj', ['tsCnpj', 'xsd:string'], 0, 0, {'name': 'Cnpj', 'type': 'xsd:string'}, None),
        MemberSpec_('InscricaoMunicipal', ['tsInscricaoMunicipal', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'InscricaoMunicipal', 'type': 'xsd:string'}, None),
        MemberSpec_('CodigoMunicipio', ['tsCodigoMunicipioIbge', 'xsd:int'], 0, 0, {'name': 'CodigoMunicipio', 'type': 'xsd:int'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Numero=None, Cnpj=None, InscricaoMunicipal=None, CodigoMunicipio=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Numero = Numero
        self.validate_tsNumeroNfse(self.Numero)
        self.Numero_nsprefix_ = None
        self.Cnpj = Cnpj
        self.validate_tsCnpj(self.Cnpj)
        self.Cnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        self.InscricaoMunicipal_nsprefix_ = None
        self.CodigoMunicipio = CodigoMunicipio
        self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
        self.CodigoMunicipio_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoNfse.subclass:
            return tcIdentificacaoNfse.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsNumeroNfse(self, value):
        result = True
        # Validate type tsNumeroNfse, a restriction on xsd:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsNumeroNfse' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsCnpj(self, value):
        result = True
        # Validate type tsCnpj, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsCnpj' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsInscricaoMunicipal(self, value):
        result = True
        # Validate type tsInscricaoMunicipal, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsCodigoMunicipioIbge(self, value):
        result = True
        # Validate type tsCodigoMunicipioIbge, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsCodigoMunicipioIbge' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Numero is not None or
            self.Cnpj is not None or
            self.InscricaoMunicipal is not None or
            self.CodigoMunicipio is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcIdentificacaoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_format_integer(self.Numero, input_name='Numero'), namespaceprefix_ , eol_))
        if self.Cnpj is not None:
            namespaceprefix_ = self.Cnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnpj_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnpj>%s</%sCnpj>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cnpj), input_name='Cnpj')), namespaceprefix_ , eol_))
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
        if self.CodigoMunicipio is not None:
            namespaceprefix_ = self.CodigoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoMunicipio>%s</%sCodigoMunicipio>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoMunicipio, input_name='CodigoMunicipio'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Numero' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Numero')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'Numero')
            self.Numero = ival_
            self.Numero_nsprefix_ = child_.prefix
            # validate type tsNumeroNfse
            self.validate_tsNumeroNfse(self.Numero)
        elif nodeName_ == 'Cnpj':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnpj')
            value_ = self.gds_validate_string(value_, node, 'Cnpj')
            self.Cnpj = value_
            self.Cnpj_nsprefix_ = child_.prefix
            # validate type tsCnpj
            self.validate_tsCnpj(self.Cnpj)
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
            # validate type tsInscricaoMunicipal
            self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        elif nodeName_ == 'CodigoMunicipio' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoMunicipio')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoMunicipio')
            self.CodigoMunicipio = ival_
            self.CodigoMunicipio_nsprefix_ = child_.prefix
            # validate type tsCodigoMunicipioIbge
            self.validate_tsCodigoMunicipioIbge(self.CodigoMunicipio)
# end class tcIdentificacaoNfse


class tcInfNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'tsIdTag', 0, 1, {'use': 'optional'}),
        MemberSpec_('Numero', ['tsNumeroNfse', 'xsd:nonNegativeInteger'], 0, 0, {'name': 'Numero', 'type': 'xsd:nonNegativeInteger'}, None),
        MemberSpec_('CodigoVerificacao', ['tsCodigoVerificacao', 'xsd:string'], 0, 0, {'name': 'CodigoVerificacao', 'type': 'xsd:string'}, None),
        MemberSpec_('DataEmissao', 'xsd:dateTime', 0, 0, {'name': 'DataEmissao', 'type': 'xsd:dateTime'}, None),
        MemberSpec_('IdentificacaoRps', 'tcIdentificacaoRps', 0, 1, {'minOccurs': '0', 'name': 'IdentificacaoRps', 'type': 'tcIdentificacaoRps'}, None),
        MemberSpec_('DataEmissaoRps', 'xsd:date', 0, 1, {'minOccurs': '0', 'name': 'DataEmissaoRps', 'type': 'xsd:date'}, None),
        MemberSpec_('NaturezaOperacao', ['tsNaturezaOperacao', 'xsd:byte'], 0, 0, {'name': 'NaturezaOperacao', 'type': 'xsd:byte'}, None),
        MemberSpec_('RegimeEspecialTributacao', ['tsRegimeEspecialTributacao', 'xsd:byte'], 0, 1, {'minOccurs': '0', 'name': 'RegimeEspecialTributacao', 'type': 'xsd:byte'}, None),
        MemberSpec_('OptanteSimplesNacional', ['tsSimNao', 'xsd:byte'], 0, 0, {'name': 'OptanteSimplesNacional', 'type': 'xsd:byte'}, None),
        MemberSpec_('IncentivadorCultural', ['tsSimNao', 'xsd:byte'], 0, 0, {'name': 'IncentivadorCultural', 'type': 'xsd:byte'}, None),
        MemberSpec_('Competencia', 'xsd:string', 0, 0, {'name': 'Competencia', 'type': 'xsd:string'}, None),
        MemberSpec_('NfseSubstituida', ['tsNumeroNfse', 'xsd:nonNegativeInteger'], 0, 1, {'minOccurs': '0', 'name': 'NfseSubstituida', 'type': 'xsd:nonNegativeInteger'}, None),
        MemberSpec_('OutrasInformacoes', ['tsOutrasInformacoes', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'OutrasInformacoes', 'type': 'xsd:string'}, None),
        MemberSpec_('Servico', 'tcDadosServico', 0, 0, {'name': 'Servico', 'type': 'tcDadosServico'}, None),
        MemberSpec_('ValorCredito', ['tsValor', 'xsd:decimal'], 0, 1, {'minOccurs': '0', 'name': 'ValorCredito', 'type': 'xsd:decimal'}, None),
        MemberSpec_('PrestadorServico', 'tcDadosPrestador', 0, 0, {'name': 'PrestadorServico', 'type': 'tcDadosPrestador'}, None),
        MemberSpec_('TomadorServico', 'tcDadosTomador', 0, 0, {'name': 'TomadorServico', 'type': 'tcDadosTomador'}, None),
        MemberSpec_('IntermediarioServico', 'tcIdentificacaoIntermediarioServico', 0, 1, {'minOccurs': '0', 'name': 'IntermediarioServico', 'type': 'tcIdentificacaoIntermediarioServico'}, None),
        MemberSpec_('OrgaoGerador', 'tcIdentificacaoOrgaoGerador', 0, 0, {'name': 'OrgaoGerador', 'type': 'tcIdentificacaoOrgaoGerador'}, None),
        MemberSpec_('ConstrucaoCivil', 'tcDadosConstrucaoCivil', 0, 1, {'minOccurs': '0', 'name': 'ConstrucaoCivil', 'type': 'tcDadosConstrucaoCivil'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, Numero=None, CodigoVerificacao=None, DataEmissao=None, IdentificacaoRps=None, DataEmissaoRps=None, NaturezaOperacao=None, RegimeEspecialTributacao=None, OptanteSimplesNacional=None, IncentivadorCultural=None, Competencia=None, NfseSubstituida=None, OutrasInformacoes=None, Servico=None, ValorCredito=None, PrestadorServico=None, TomadorServico=None, IntermediarioServico=None, OrgaoGerador=None, ConstrucaoCivil=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.Numero = Numero
        self.validate_tsNumeroNfse(self.Numero)
        self.Numero_nsprefix_ = None
        self.CodigoVerificacao = CodigoVerificacao
        self.validate_tsCodigoVerificacao(self.CodigoVerificacao)
        self.CodigoVerificacao_nsprefix_ = None
        if isinstance(DataEmissao, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissao, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEmissao
        self.DataEmissao = initvalue_
        self.DataEmissao_nsprefix_ = None
        self.IdentificacaoRps = IdentificacaoRps
        self.IdentificacaoRps_nsprefix_ = None
        if isinstance(DataEmissaoRps, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissaoRps, '%Y-%m-%d').date()
        else:
            initvalue_ = DataEmissaoRps
        self.DataEmissaoRps = initvalue_
        self.DataEmissaoRps_nsprefix_ = None
        self.NaturezaOperacao = NaturezaOperacao
        self.validate_tsNaturezaOperacao(self.NaturezaOperacao)
        self.NaturezaOperacao_nsprefix_ = None
        self.RegimeEspecialTributacao = RegimeEspecialTributacao
        self.validate_tsRegimeEspecialTributacao(self.RegimeEspecialTributacao)
        self.RegimeEspecialTributacao_nsprefix_ = None
        self.OptanteSimplesNacional = OptanteSimplesNacional
        self.validate_tsSimNao(self.OptanteSimplesNacional)
        self.OptanteSimplesNacional_nsprefix_ = None
        self.IncentivadorCultural = IncentivadorCultural
        self.validate_tsSimNao(self.IncentivadorCultural)
        self.IncentivadorCultural_nsprefix_ = None
        self.Competencia = Competencia
        self.Competencia_nsprefix_ = None
        self.NfseSubstituida = NfseSubstituida
        self.validate_tsNumeroNfse(self.NfseSubstituida)
        self.NfseSubstituida_nsprefix_ = None
        self.OutrasInformacoes = OutrasInformacoes
        self.validate_tsOutrasInformacoes(self.OutrasInformacoes)
        self.OutrasInformacoes_nsprefix_ = None
        self.Servico = Servico
        self.Servico_nsprefix_ = None
        self.ValorCredito = ValorCredito
        self.validate_tsValor(self.ValorCredito)
        self.ValorCredito_nsprefix_ = None
        self.PrestadorServico = PrestadorServico
        self.PrestadorServico_nsprefix_ = None
        self.TomadorServico = TomadorServico
        self.TomadorServico_nsprefix_ = None
        self.IntermediarioServico = IntermediarioServico
        self.IntermediarioServico_nsprefix_ = None
        self.OrgaoGerador = OrgaoGerador
        self.OrgaoGerador_nsprefix_ = None
        self.ConstrucaoCivil = ConstrucaoCivil
        self.ConstrucaoCivil_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfNfse.subclass:
            return tcInfNfse.subclass(*args_, **kwargs_)
        else:
            return tcInfNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsNumeroNfse(self, value):
        result = True
        # Validate type tsNumeroNfse, a restriction on xsd:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsNumeroNfse' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsCodigoVerificacao(self, value):
        result = True
        # Validate type tsCodigoVerificacao, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsCodigoVerificacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsCodigoVerificacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsNaturezaOperacao(self, value):
        result = True
        # Validate type tsNaturezaOperacao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsNaturezaOperacao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsNaturezaOperacao_patterns_, ))
                result = False
        return result
    validate_tsNaturezaOperacao_patterns_ = [['^(1|2|3|4|5|6)$']]
    def validate_tsRegimeEspecialTributacao(self, value):
        result = True
        # Validate type tsRegimeEspecialTributacao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsRegimeEspecialTributacao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsRegimeEspecialTributacao_patterns_, ))
                result = False
        return result
    validate_tsRegimeEspecialTributacao_patterns_ = [['^(0|1|2|3|4|5|6)$']]
    def validate_tsSimNao(self, value):
        result = True
        # Validate type tsSimNao, a restriction on xsd:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tsSimNao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tsSimNao_patterns_, ))
                result = False
        return result
    validate_tsSimNao_patterns_ = [['^(1|2)$']]
    def validate_tsOutrasInformacoes(self, value):
        result = True
        # Validate type tsOutrasInformacoes, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsOutrasInformacoes' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsOutrasInformacoes' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsValor(self, value):
        result = True
        # Validate type tsValor, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tsValor' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsValor' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsIdTag(self, value):
        # Validate type tsIdTag, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsIdTag' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.Numero is not None or
            self.CodigoVerificacao is not None or
            self.DataEmissao is not None or
            self.IdentificacaoRps is not None or
            self.DataEmissaoRps is not None or
            self.NaturezaOperacao is not None or
            self.RegimeEspecialTributacao is not None or
            self.OptanteSimplesNacional is not None or
            self.IncentivadorCultural is not None or
            self.Competencia is not None or
            self.NfseSubstituida is not None or
            self.OutrasInformacoes is not None or
            self.Servico is not None or
            self.ValorCredito is not None or
            self.PrestadorServico is not None or
            self.TomadorServico is not None or
            self.IntermediarioServico is not None or
            self.OrgaoGerador is not None or
            self.ConstrucaoCivil is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfNfse'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_format_integer(self.Numero, input_name='Numero'), namespaceprefix_ , eol_))
        if self.CodigoVerificacao is not None:
            namespaceprefix_ = self.CodigoVerificacao_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoVerificacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoVerificacao>%s</%sCodigoVerificacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoVerificacao), input_name='CodigoVerificacao')), namespaceprefix_ , eol_))
        if self.DataEmissao is not None:
            namespaceprefix_ = self.DataEmissao_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissao>%s</%sDataEmissao>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEmissao, input_name='DataEmissao'), namespaceprefix_ , eol_))
        if self.IdentificacaoRps is not None:
            namespaceprefix_ = self.IdentificacaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoRps_nsprefix_) else ''
            self.IdentificacaoRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoRps', pretty_print=pretty_print)
        if self.DataEmissaoRps is not None:
            namespaceprefix_ = self.DataEmissaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissaoRps_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissaoRps>%s</%sDataEmissaoRps>%s' % (namespaceprefix_ , self.gds_format_date(self.DataEmissaoRps, input_name='DataEmissaoRps'), namespaceprefix_ , eol_))
        if self.NaturezaOperacao is not None:
            namespaceprefix_ = self.NaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.NaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaturezaOperacao>%s</%sNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.NaturezaOperacao, input_name='NaturezaOperacao'), namespaceprefix_ , eol_))
        if self.RegimeEspecialTributacao is not None:
            namespaceprefix_ = self.RegimeEspecialTributacao_nsprefix_ + ':' if (UseCapturedNS_ and self.RegimeEspecialTributacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRegimeEspecialTributacao>%s</%sRegimeEspecialTributacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.RegimeEspecialTributacao, input_name='RegimeEspecialTributacao'), namespaceprefix_ , eol_))
        if self.OptanteSimplesNacional is not None:
            namespaceprefix_ = self.OptanteSimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.OptanteSimplesNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOptanteSimplesNacional>%s</%sOptanteSimplesNacional>%s' % (namespaceprefix_ , self.gds_format_integer(self.OptanteSimplesNacional, input_name='OptanteSimplesNacional'), namespaceprefix_ , eol_))
        if self.IncentivadorCultural is not None:
            namespaceprefix_ = self.IncentivadorCultural_nsprefix_ + ':' if (UseCapturedNS_ and self.IncentivadorCultural_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIncentivadorCultural>%s</%sIncentivadorCultural>%s' % (namespaceprefix_ , self.gds_format_integer(self.IncentivadorCultural, input_name='IncentivadorCultural'), namespaceprefix_ , eol_))
        if self.Competencia is not None:
            namespaceprefix_ = self.Competencia_nsprefix_ + ':' if (UseCapturedNS_ and self.Competencia_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCompetencia>%s</%sCompetencia>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Competencia), input_name='Competencia')), namespaceprefix_ , eol_))
        if self.NfseSubstituida is not None:
            namespaceprefix_ = self.NfseSubstituida_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseSubstituida_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNfseSubstituida>%s</%sNfseSubstituida>%s' % (namespaceprefix_ , self.gds_format_integer(self.NfseSubstituida, input_name='NfseSubstituida'), namespaceprefix_ , eol_))
        if self.OutrasInformacoes is not None:
            namespaceprefix_ = self.OutrasInformacoes_nsprefix_ + ':' if (UseCapturedNS_ and self.OutrasInformacoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOutrasInformacoes>%s</%sOutrasInformacoes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OutrasInformacoes), input_name='OutrasInformacoes')), namespaceprefix_ , eol_))
        if self.Servico is not None:
            namespaceprefix_ = self.Servico_nsprefix_ + ':' if (UseCapturedNS_ and self.Servico_nsprefix_) else ''
            self.Servico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Servico', pretty_print=pretty_print)
        if self.ValorCredito is not None:
            namespaceprefix_ = self.ValorCredito_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCredito_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCredito>%s</%sValorCredito>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCredito, input_name='ValorCredito'), namespaceprefix_ , eol_))
        if self.PrestadorServico is not None:
            namespaceprefix_ = self.PrestadorServico_nsprefix_ + ':' if (UseCapturedNS_ and self.PrestadorServico_nsprefix_) else ''
            self.PrestadorServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PrestadorServico', pretty_print=pretty_print)
        if self.TomadorServico is not None:
            namespaceprefix_ = self.TomadorServico_nsprefix_ + ':' if (UseCapturedNS_ and self.TomadorServico_nsprefix_) else ''
            self.TomadorServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TomadorServico', pretty_print=pretty_print)
        if self.IntermediarioServico is not None:
            namespaceprefix_ = self.IntermediarioServico_nsprefix_ + ':' if (UseCapturedNS_ and self.IntermediarioServico_nsprefix_) else ''
            self.IntermediarioServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IntermediarioServico', pretty_print=pretty_print)
        if self.OrgaoGerador is not None:
            namespaceprefix_ = self.OrgaoGerador_nsprefix_ + ':' if (UseCapturedNS_ and self.OrgaoGerador_nsprefix_) else ''
            self.OrgaoGerador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrgaoGerador', pretty_print=pretty_print)
        if self.ConstrucaoCivil is not None:
            namespaceprefix_ = self.ConstrucaoCivil_nsprefix_ + ':' if (UseCapturedNS_ and self.ConstrucaoCivil_nsprefix_) else ''
            self.ConstrucaoCivil.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ConstrucaoCivil', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_tsIdTag(self.Id)    # validate type tsIdTag
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Numero' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Numero')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'Numero')
            self.Numero = ival_
            self.Numero_nsprefix_ = child_.prefix
            # validate type tsNumeroNfse
            self.validate_tsNumeroNfse(self.Numero)
        elif nodeName_ == 'CodigoVerificacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoVerificacao')
            value_ = self.gds_validate_string(value_, node, 'CodigoVerificacao')
            self.CodigoVerificacao = value_
            self.CodigoVerificacao_nsprefix_ = child_.prefix
            # validate type tsCodigoVerificacao
            self.validate_tsCodigoVerificacao(self.CodigoVerificacao)
        elif nodeName_ == 'DataEmissao':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEmissao = dval_
            self.DataEmissao_nsprefix_ = child_.prefix
        elif nodeName_ == 'IdentificacaoRps':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoRps = obj_
            obj_.original_tagname_ = 'IdentificacaoRps'
        elif nodeName_ == 'DataEmissaoRps':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.DataEmissaoRps = dval_
            self.DataEmissaoRps_nsprefix_ = child_.prefix
        elif nodeName_ == 'NaturezaOperacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NaturezaOperacao')
            ival_ = self.gds_validate_integer(ival_, node, 'NaturezaOperacao')
            self.NaturezaOperacao = ival_
            self.NaturezaOperacao_nsprefix_ = child_.prefix
            # validate type tsNaturezaOperacao
            self.validate_tsNaturezaOperacao(self.NaturezaOperacao)
        elif nodeName_ == 'RegimeEspecialTributacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'RegimeEspecialTributacao')
            ival_ = self.gds_validate_integer(ival_, node, 'RegimeEspecialTributacao')
            self.RegimeEspecialTributacao = ival_
            self.RegimeEspecialTributacao_nsprefix_ = child_.prefix
            # validate type tsRegimeEspecialTributacao
            self.validate_tsRegimeEspecialTributacao(self.RegimeEspecialTributacao)
        elif nodeName_ == 'OptanteSimplesNacional' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'OptanteSimplesNacional')
            ival_ = self.gds_validate_integer(ival_, node, 'OptanteSimplesNacional')
            self.OptanteSimplesNacional = ival_
            self.OptanteSimplesNacional_nsprefix_ = child_.prefix
            # validate type tsSimNao
            self.validate_tsSimNao(self.OptanteSimplesNacional)
        elif nodeName_ == 'IncentivadorCultural' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'IncentivadorCultural')
            ival_ = self.gds_validate_integer(ival_, node, 'IncentivadorCultural')
            self.IncentivadorCultural = ival_
            self.IncentivadorCultural_nsprefix_ = child_.prefix
            # validate type tsSimNao
            self.validate_tsSimNao(self.IncentivadorCultural)
        elif nodeName_ == 'Competencia':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Competencia')
            value_ = self.gds_validate_string(value_, node, 'Competencia')
            self.Competencia = value_
            self.Competencia_nsprefix_ = child_.prefix
        elif nodeName_ == 'NfseSubstituida' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NfseSubstituida')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'NfseSubstituida')
            self.NfseSubstituida = ival_
            self.NfseSubstituida_nsprefix_ = child_.prefix
            # validate type tsNumeroNfse
            self.validate_tsNumeroNfse(self.NfseSubstituida)
        elif nodeName_ == 'OutrasInformacoes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OutrasInformacoes')
            value_ = self.gds_validate_string(value_, node, 'OutrasInformacoes')
            self.OutrasInformacoes = value_
            self.OutrasInformacoes_nsprefix_ = child_.prefix
            # validate type tsOutrasInformacoes
            self.validate_tsOutrasInformacoes(self.OutrasInformacoes)
        elif nodeName_ == 'Servico':
            obj_ = tcDadosServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Servico = obj_
            obj_.original_tagname_ = 'Servico'
        elif nodeName_ == 'ValorCredito' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCredito')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCredito')
            self.ValorCredito = fval_
            self.ValorCredito_nsprefix_ = child_.prefix
            # validate type tsValor
            self.validate_tsValor(self.ValorCredito)
        elif nodeName_ == 'PrestadorServico':
            obj_ = tcDadosPrestador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PrestadorServico = obj_
            obj_.original_tagname_ = 'PrestadorServico'
        elif nodeName_ == 'TomadorServico':
            obj_ = tcDadosTomador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TomadorServico = obj_
            obj_.original_tagname_ = 'TomadorServico'
        elif nodeName_ == 'IntermediarioServico':
            obj_ = tcIdentificacaoIntermediarioServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IntermediarioServico = obj_
            obj_.original_tagname_ = 'IntermediarioServico'
        elif nodeName_ == 'OrgaoGerador':
            obj_ = tcIdentificacaoOrgaoGerador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrgaoGerador = obj_
            obj_.original_tagname_ = 'OrgaoGerador'
        elif nodeName_ == 'ConstrucaoCivil':
            obj_ = tcDadosConstrucaoCivil.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ConstrucaoCivil = obj_
            obj_.original_tagname_ = 'ConstrucaoCivil'
# end class tcInfNfse


class tcNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('InfNfse', 'tcInfNfse', 0, 0, {'name': 'InfNfse', 'type': 'tcInfNfse'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, InfNfse=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InfNfse = InfNfse
        self.InfNfse_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcNfse.subclass:
            return tcNfse.subclass(*args_, **kwargs_)
        else:
            return tcNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.InfNfse is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InfNfse is not None:
            namespaceprefix_ = self.InfNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.InfNfse_nsprefix_) else ''
            self.InfNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfNfse', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='dsig:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InfNfse':
            obj_ = tcInfNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfNfse = obj_
            obj_.original_tagname_ = 'InfNfse'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class tcNfse


class tcInfPedidoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'tsIdTag', 0, 1, {'use': 'optional'}),
        MemberSpec_('IdentificacaoNfse', 'tcIdentificacaoNfse', 0, 0, {'name': 'IdentificacaoNfse', 'type': 'tcIdentificacaoNfse'}, None),
        MemberSpec_('CodigoCancelamento', ['tsCodigoCancelamentoNfse', 'xsd:string'], 0, 0, {'name': 'CodigoCancelamento', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, IdentificacaoNfse=None, CodigoCancelamento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.IdentificacaoNfse = IdentificacaoNfse
        self.IdentificacaoNfse_nsprefix_ = None
        self.CodigoCancelamento = CodigoCancelamento
        self.validate_tsCodigoCancelamentoNfse(self.CodigoCancelamento)
        self.CodigoCancelamento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfPedidoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfPedidoCancelamento.subclass:
            return tcInfPedidoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcInfPedidoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCodigoCancelamentoNfse(self, value):
        result = True
        # Validate type tsCodigoCancelamentoNfse, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsCodigoCancelamentoNfse' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsCodigoCancelamentoNfse' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsIdTag(self, value):
        # Validate type tsIdTag, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsIdTag' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.IdentificacaoNfse is not None or
            self.CodigoCancelamento is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfPedidoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfPedidoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfPedidoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfPedidoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfPedidoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfPedidoCancelamento'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfPedidoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoNfse is not None:
            namespaceprefix_ = self.IdentificacaoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoNfse_nsprefix_) else ''
            self.IdentificacaoNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoNfse', pretty_print=pretty_print)
        if self.CodigoCancelamento is not None:
            namespaceprefix_ = self.CodigoCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCancelamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCancelamento>%s</%sCodigoCancelamento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoCancelamento), input_name='CodigoCancelamento')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_tsIdTag(self.Id)    # validate type tsIdTag
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoNfse':
            obj_ = tcIdentificacaoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoNfse = obj_
            obj_.original_tagname_ = 'IdentificacaoNfse'
        elif nodeName_ == 'CodigoCancelamento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoCancelamento')
            value_ = self.gds_validate_string(value_, node, 'CodigoCancelamento')
            self.CodigoCancelamento = value_
            self.CodigoCancelamento_nsprefix_ = child_.prefix
            # validate type tsCodigoCancelamentoNfse
            self.validate_tsCodigoCancelamentoNfse(self.CodigoCancelamento)
# end class tcInfPedidoCancelamento


class tcPedidoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('InfPedidoCancelamento', 'tcInfPedidoCancelamento', 0, 0, {'name': 'InfPedidoCancelamento', 'type': 'tcInfPedidoCancelamento'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, InfPedidoCancelamento=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InfPedidoCancelamento = InfPedidoCancelamento
        self.InfPedidoCancelamento_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcPedidoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcPedidoCancelamento.subclass:
            return tcPedidoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcPedidoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.InfPedidoCancelamento is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcPedidoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcPedidoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcPedidoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcPedidoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcPedidoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcPedidoCancelamento'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcPedidoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InfPedidoCancelamento is not None:
            namespaceprefix_ = self.InfPedidoCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.InfPedidoCancelamento_nsprefix_) else ''
            self.InfPedidoCancelamento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfPedidoCancelamento', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='dsig:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InfPedidoCancelamento':
            obj_ = tcInfPedidoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfPedidoCancelamento = obj_
            obj_.original_tagname_ = 'InfPedidoCancelamento'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class tcPedidoCancelamento


class tcInfConfirmacaoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Sucesso', 'xsd:boolean', 0, 0, {'name': 'Sucesso', 'type': 'xsd:boolean'}, None),
        MemberSpec_('DataHora', 'xsd:dateTime', 0, 0, {'name': 'DataHora', 'type': 'xsd:dateTime'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Sucesso=None, DataHora=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Sucesso = Sucesso
        self.Sucesso_nsprefix_ = None
        if isinstance(DataHora, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataHora, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataHora
        self.DataHora = initvalue_
        self.DataHora_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfConfirmacaoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfConfirmacaoCancelamento.subclass:
            return tcInfConfirmacaoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcInfConfirmacaoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Sucesso is not None or
            self.DataHora is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfConfirmacaoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfConfirmacaoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfConfirmacaoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfConfirmacaoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfConfirmacaoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfConfirmacaoCancelamento'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfConfirmacaoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Sucesso is not None:
            namespaceprefix_ = self.Sucesso_nsprefix_ + ':' if (UseCapturedNS_ and self.Sucesso_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSucesso>%s</%sSucesso>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Sucesso, input_name='Sucesso'), namespaceprefix_ , eol_))
        if self.DataHora is not None:
            namespaceprefix_ = self.DataHora_nsprefix_ + ':' if (UseCapturedNS_ and self.DataHora_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataHora>%s</%sDataHora>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataHora, input_name='DataHora'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Sucesso':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Sucesso')
            ival_ = self.gds_validate_boolean(ival_, node, 'Sucesso')
            self.Sucesso = ival_
            self.Sucesso_nsprefix_ = child_.prefix
        elif nodeName_ == 'DataHora':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataHora = dval_
            self.DataHora_nsprefix_ = child_.prefix
# end class tcInfConfirmacaoCancelamento


class tcConfirmacaoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'tsIdTag', 0, 1, {'use': 'optional'}),
        MemberSpec_('Pedido', 'tcPedidoCancelamento', 0, 0, {'name': 'Pedido', 'type': 'tcPedidoCancelamento'}, None),
        MemberSpec_('InfConfirmacaoCancelamento', 'tcInfConfirmacaoCancelamento', 0, 0, {'name': 'InfConfirmacaoCancelamento', 'type': 'tcInfConfirmacaoCancelamento'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, Pedido=None, InfConfirmacaoCancelamento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.Pedido = Pedido
        self.Pedido_nsprefix_ = None
        self.InfConfirmacaoCancelamento = InfConfirmacaoCancelamento
        self.InfConfirmacaoCancelamento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcConfirmacaoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcConfirmacaoCancelamento.subclass:
            return tcConfirmacaoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcConfirmacaoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsIdTag(self, value):
        # Validate type tsIdTag, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsIdTag' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.Pedido is not None or
            self.InfConfirmacaoCancelamento is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcConfirmacaoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcConfirmacaoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcConfirmacaoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcConfirmacaoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcConfirmacaoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcConfirmacaoCancelamento'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcConfirmacaoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Pedido is not None:
            namespaceprefix_ = self.Pedido_nsprefix_ + ':' if (UseCapturedNS_ and self.Pedido_nsprefix_) else ''
            self.Pedido.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Pedido', pretty_print=pretty_print)
        if self.InfConfirmacaoCancelamento is not None:
            namespaceprefix_ = self.InfConfirmacaoCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.InfConfirmacaoCancelamento_nsprefix_) else ''
            self.InfConfirmacaoCancelamento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfConfirmacaoCancelamento', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_tsIdTag(self.Id)    # validate type tsIdTag
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Pedido':
            obj_ = tcPedidoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Pedido = obj_
            obj_.original_tagname_ = 'Pedido'
        elif nodeName_ == 'InfConfirmacaoCancelamento':
            obj_ = tcInfConfirmacaoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfConfirmacaoCancelamento = obj_
            obj_.original_tagname_ = 'InfConfirmacaoCancelamento'
# end class tcConfirmacaoCancelamento


class tcCancelamentoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Confirmacao', 'tcConfirmacaoCancelamento', 0, 0, {'name': 'Confirmacao', 'type': 'tcConfirmacaoCancelamento'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Confirmacao=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Confirmacao = Confirmacao
        self.Confirmacao_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCancelamentoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCancelamentoNfse.subclass:
            return tcCancelamentoNfse.subclass(*args_, **kwargs_)
        else:
            return tcCancelamentoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Confirmacao is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcCancelamentoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCancelamentoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCancelamentoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCancelamentoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCancelamentoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCancelamentoNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcCancelamentoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Confirmacao is not None:
            namespaceprefix_ = self.Confirmacao_nsprefix_ + ':' if (UseCapturedNS_ and self.Confirmacao_nsprefix_) else ''
            self.Confirmacao.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Confirmacao', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='dsig:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Confirmacao':
            obj_ = tcConfirmacaoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Confirmacao = obj_
            obj_.original_tagname_ = 'Confirmacao'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class tcCancelamentoNfse


class tcInfSubstituicaoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'tsIdTag', 0, 1, {'use': 'optional'}),
        MemberSpec_('NfseSubstituidora', ['tsNumeroNfse', 'xsd:nonNegativeInteger'], 0, 0, {'name': 'NfseSubstituidora', 'type': 'xsd:nonNegativeInteger'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, NfseSubstituidora=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.NfseSubstituidora = NfseSubstituidora
        self.validate_tsNumeroNfse(self.NfseSubstituidora)
        self.NfseSubstituidora_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfSubstituicaoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfSubstituicaoNfse.subclass:
            return tcInfSubstituicaoNfse.subclass(*args_, **kwargs_)
        else:
            return tcInfSubstituicaoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsNumeroNfse(self, value):
        result = True
        # Validate type tsNumeroNfse, a restriction on xsd:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsNumeroNfse' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsIdTag(self, value):
        # Validate type tsIdTag, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsIdTag' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.NfseSubstituidora is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfSubstituicaoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfSubstituicaoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfSubstituicaoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfSubstituicaoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfSubstituicaoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfSubstituicaoNfse'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcInfSubstituicaoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NfseSubstituidora is not None:
            namespaceprefix_ = self.NfseSubstituidora_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseSubstituidora_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNfseSubstituidora>%s</%sNfseSubstituidora>%s' % (namespaceprefix_ , self.gds_format_integer(self.NfseSubstituidora, input_name='NfseSubstituidora'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_tsIdTag(self.Id)    # validate type tsIdTag
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NfseSubstituidora' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NfseSubstituidora')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'NfseSubstituidora')
            self.NfseSubstituidora = ival_
            self.NfseSubstituidora_nsprefix_ = child_.prefix
            # validate type tsNumeroNfse
            self.validate_tsNumeroNfse(self.NfseSubstituidora)
# end class tcInfSubstituicaoNfse


class tcSubstituicaoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('SubstituicaoNfse', 'tcInfSubstituicaoNfse', 0, 0, {'name': 'SubstituicaoNfse', 'type': 'tcInfSubstituicaoNfse'}, None),
        MemberSpec_('Signature', 'SignatureType', 1, 0, {'maxOccurs': '2', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, SubstituicaoNfse=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.SubstituicaoNfse = SubstituicaoNfse
        self.SubstituicaoNfse_nsprefix_ = None
        if Signature is None:
            self.Signature = []
        else:
            self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcSubstituicaoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcSubstituicaoNfse.subclass:
            return tcSubstituicaoNfse.subclass(*args_, **kwargs_)
        else:
            return tcSubstituicaoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.SubstituicaoNfse is not None or
            self.Signature
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcSubstituicaoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcSubstituicaoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcSubstituicaoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcSubstituicaoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcSubstituicaoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcSubstituicaoNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcSubstituicaoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SubstituicaoNfse is not None:
            namespaceprefix_ = self.SubstituicaoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.SubstituicaoNfse_nsprefix_) else ''
            self.SubstituicaoNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SubstituicaoNfse', pretty_print=pretty_print)
        for Signature_ in self.Signature:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            Signature_.export(outfile, level, namespaceprefix_='dsig:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SubstituicaoNfse':
            obj_ = tcInfSubstituicaoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SubstituicaoNfse = obj_
            obj_.original_tagname_ = 'SubstituicaoNfse'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature.append(obj_)
            obj_.original_tagname_ = 'Signature'
# end class tcSubstituicaoNfse


class tcCompNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Nfse', 'tcNfse', 0, 0, {'name': 'Nfse', 'type': 'tcNfse'}, None),
        MemberSpec_('NfseCancelamento', 'tcCancelamentoNfse', 0, 1, {'minOccurs': '0', 'name': 'NfseCancelamento', 'type': 'tcCancelamentoNfse'}, None),
        MemberSpec_('NfseSubstituicao', 'tcSubstituicaoNfse', 0, 1, {'minOccurs': '0', 'name': 'NfseSubstituicao', 'type': 'tcSubstituicaoNfse'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Nfse=None, NfseCancelamento=None, NfseSubstituicao=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Nfse = Nfse
        self.Nfse_nsprefix_ = None
        self.NfseCancelamento = NfseCancelamento
        self.NfseCancelamento_nsprefix_ = None
        self.NfseSubstituicao = NfseSubstituicao
        self.NfseSubstituicao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCompNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCompNfse.subclass:
            return tcCompNfse.subclass(*args_, **kwargs_)
        else:
            return tcCompNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Nfse is not None or
            self.NfseCancelamento is not None or
            self.NfseSubstituicao is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcCompNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCompNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCompNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCompNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCompNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCompNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcCompNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Nfse is not None:
            namespaceprefix_ = self.Nfse_nsprefix_ + ':' if (UseCapturedNS_ and self.Nfse_nsprefix_) else ''
            self.Nfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Nfse', pretty_print=pretty_print)
        if self.NfseCancelamento is not None:
            namespaceprefix_ = self.NfseCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseCancelamento_nsprefix_) else ''
            self.NfseCancelamento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NfseCancelamento', pretty_print=pretty_print)
        if self.NfseSubstituicao is not None:
            namespaceprefix_ = self.NfseSubstituicao_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseSubstituicao_nsprefix_) else ''
            self.NfseSubstituicao.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NfseSubstituicao', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Nfse':
            obj_ = tcNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Nfse = obj_
            obj_.original_tagname_ = 'Nfse'
        elif nodeName_ == 'NfseCancelamento':
            obj_ = tcCancelamentoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NfseCancelamento = obj_
            obj_.original_tagname_ = 'NfseCancelamento'
        elif nodeName_ == 'NfseSubstituicao':
            obj_ = tcSubstituicaoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NfseSubstituicao = obj_
            obj_.original_tagname_ = 'NfseSubstituicao'
# end class tcCompNfse


class ListaMensagemRetorno(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('MensagemRetorno', 'tcMensagemRetorno', 1, 0, {'maxOccurs': 'unbounded', 'name': 'MensagemRetorno', 'type': 'tcMensagemRetorno'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, MensagemRetorno=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if MensagemRetorno is None:
            self.MensagemRetorno = []
        else:
            self.MensagemRetorno = MensagemRetorno
        self.MensagemRetorno_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaMensagemRetorno)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaMensagemRetorno.subclass:
            return ListaMensagemRetorno.subclass(*args_, **kwargs_)
        else:
            return ListaMensagemRetorno(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.MensagemRetorno
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListaMensagemRetorno', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaMensagemRetorno')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaMensagemRetorno':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaMensagemRetorno')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaMensagemRetorno', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaMensagemRetorno'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListaMensagemRetorno', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for MensagemRetorno_ in self.MensagemRetorno:
            namespaceprefix_ = self.MensagemRetorno_nsprefix_ + ':' if (UseCapturedNS_ and self.MensagemRetorno_nsprefix_) else ''
            MensagemRetorno_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MensagemRetorno', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MensagemRetorno':
            obj_ = tcMensagemRetorno.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MensagemRetorno.append(obj_)
            obj_.original_tagname_ = 'MensagemRetorno'
# end class ListaMensagemRetorno


class tcMensagemRetorno(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Codigo', ['tsCodigoMensagemAlerta', 'xsd:string'], 0, 0, {'name': 'Codigo', 'type': 'xsd:string'}, None),
        MemberSpec_('Mensagem', ['tsDescricaoMensagemAlerta', 'xsd:string'], 0, 0, {'name': 'Mensagem', 'type': 'xsd:string'}, None),
        MemberSpec_('Correcao', ['tsDescricaoMensagemAlerta', 'xsd:string'], 0, 1, {'minOccurs': '0', 'name': 'Correcao', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Codigo=None, Mensagem=None, Correcao=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Codigo = Codigo
        self.validate_tsCodigoMensagemAlerta(self.Codigo)
        self.Codigo_nsprefix_ = None
        self.Mensagem = Mensagem
        self.validate_tsDescricaoMensagemAlerta(self.Mensagem)
        self.Mensagem_nsprefix_ = None
        self.Correcao = Correcao
        self.validate_tsDescricaoMensagemAlerta(self.Correcao)
        self.Correcao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcMensagemRetorno)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcMensagemRetorno.subclass:
            return tcMensagemRetorno.subclass(*args_, **kwargs_)
        else:
            return tcMensagemRetorno(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCodigoMensagemAlerta(self, value):
        result = True
        # Validate type tsCodigoMensagemAlerta, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsCodigoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsCodigoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsDescricaoMensagemAlerta(self, value):
        result = True
        # Validate type tsDescricaoMensagemAlerta, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsDescricaoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsDescricaoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Codigo is not None or
            self.Mensagem is not None or
            self.Correcao is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcMensagemRetorno', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcMensagemRetorno')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcMensagemRetorno':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcMensagemRetorno')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcMensagemRetorno', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcMensagemRetorno'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcMensagemRetorno', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Codigo is not None:
            namespaceprefix_ = self.Codigo_nsprefix_ + ':' if (UseCapturedNS_ and self.Codigo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigo>%s</%sCodigo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Codigo), input_name='Codigo')), namespaceprefix_ , eol_))
        if self.Mensagem is not None:
            namespaceprefix_ = self.Mensagem_nsprefix_ + ':' if (UseCapturedNS_ and self.Mensagem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMensagem>%s</%sMensagem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mensagem), input_name='Mensagem')), namespaceprefix_ , eol_))
        if self.Correcao is not None:
            namespaceprefix_ = self.Correcao_nsprefix_ + ':' if (UseCapturedNS_ and self.Correcao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCorrecao>%s</%sCorrecao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Correcao), input_name='Correcao')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Codigo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Codigo')
            value_ = self.gds_validate_string(value_, node, 'Codigo')
            self.Codigo = value_
            self.Codigo_nsprefix_ = child_.prefix
            # validate type tsCodigoMensagemAlerta
            self.validate_tsCodigoMensagemAlerta(self.Codigo)
        elif nodeName_ == 'Mensagem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mensagem')
            value_ = self.gds_validate_string(value_, node, 'Mensagem')
            self.Mensagem = value_
            self.Mensagem_nsprefix_ = child_.prefix
            # validate type tsDescricaoMensagemAlerta
            self.validate_tsDescricaoMensagemAlerta(self.Mensagem)
        elif nodeName_ == 'Correcao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Correcao')
            value_ = self.gds_validate_string(value_, node, 'Correcao')
            self.Correcao = value_
            self.Correcao_nsprefix_ = child_.prefix
            # validate type tsDescricaoMensagemAlerta
            self.validate_tsDescricaoMensagemAlerta(self.Correcao)
# end class tcMensagemRetorno


class tcMensagemRetornoLote(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('IdentificacaoRps', 'tcIdentificacaoRps', 0, 0, {'name': 'IdentificacaoRps', 'type': 'tcIdentificacaoRps'}, None),
        MemberSpec_('Codigo', ['tsCodigoMensagemAlerta', 'xsd:string'], 0, 0, {'name': 'Codigo', 'type': 'xsd:string'}, None),
        MemberSpec_('Mensagem', ['tsDescricaoMensagemAlerta', 'xsd:string'], 0, 0, {'name': 'Mensagem', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoRps=None, Codigo=None, Mensagem=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoRps = IdentificacaoRps
        self.IdentificacaoRps_nsprefix_ = None
        self.Codigo = Codigo
        self.validate_tsCodigoMensagemAlerta(self.Codigo)
        self.Codigo_nsprefix_ = None
        self.Mensagem = Mensagem
        self.validate_tsDescricaoMensagemAlerta(self.Mensagem)
        self.Mensagem_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcMensagemRetornoLote)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcMensagemRetornoLote.subclass:
            return tcMensagemRetornoLote.subclass(*args_, **kwargs_)
        else:
            return tcMensagemRetornoLote(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsCodigoMensagemAlerta(self, value):
        result = True
        # Validate type tsCodigoMensagemAlerta, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsCodigoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsCodigoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsDescricaoMensagemAlerta(self, value):
        result = True
        # Validate type tsDescricaoMensagemAlerta, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsDescricaoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsDescricaoMensagemAlerta' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.IdentificacaoRps is not None or
            self.Codigo is not None or
            self.Mensagem is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcMensagemRetornoLote', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcMensagemRetornoLote')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcMensagemRetornoLote':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcMensagemRetornoLote')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcMensagemRetornoLote', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcMensagemRetornoLote'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcMensagemRetornoLote', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoRps is not None:
            namespaceprefix_ = self.IdentificacaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoRps_nsprefix_) else ''
            self.IdentificacaoRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoRps', pretty_print=pretty_print)
        if self.Codigo is not None:
            namespaceprefix_ = self.Codigo_nsprefix_ + ':' if (UseCapturedNS_ and self.Codigo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigo>%s</%sCodigo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Codigo), input_name='Codigo')), namespaceprefix_ , eol_))
        if self.Mensagem is not None:
            namespaceprefix_ = self.Mensagem_nsprefix_ + ':' if (UseCapturedNS_ and self.Mensagem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMensagem>%s</%sMensagem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mensagem), input_name='Mensagem')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoRps':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoRps = obj_
            obj_.original_tagname_ = 'IdentificacaoRps'
        elif nodeName_ == 'Codigo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Codigo')
            value_ = self.gds_validate_string(value_, node, 'Codigo')
            self.Codigo = value_
            self.Codigo_nsprefix_ = child_.prefix
            # validate type tsCodigoMensagemAlerta
            self.validate_tsCodigoMensagemAlerta(self.Codigo)
        elif nodeName_ == 'Mensagem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mensagem')
            value_ = self.gds_validate_string(value_, node, 'Mensagem')
            self.Mensagem = value_
            self.Mensagem_nsprefix_ = child_.prefix
            # validate type tsDescricaoMensagemAlerta
            self.validate_tsDescricaoMensagemAlerta(self.Mensagem)
# end class tcMensagemRetornoLote


class tcLoteRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'tsIdTag', 0, 1, {'use': 'optional'}),
        MemberSpec_('NumeroLote', ['tsNumeroLote', 'xsd:nonNegativeInteger'], 0, 0, {'name': 'NumeroLote', 'type': 'xsd:nonNegativeInteger'}, None),
        MemberSpec_('Cnpj', ['tsCnpj', 'xsd:string'], 0, 0, {'name': 'Cnpj', 'type': 'xsd:string'}, None),
        MemberSpec_('InscricaoMunicipal', ['tsInscricaoMunicipal', 'xsd:string'], 0, 0, {'name': 'InscricaoMunicipal', 'type': 'xsd:string'}, None),
        MemberSpec_('QuantidadeRps', ['tsQuantidadeRps', 'xsd:int'], 0, 0, {'name': 'QuantidadeRps', 'type': 'xsd:int'}, None),
        MemberSpec_('ListaRps', 'ListaRpsType', 0, 0, {'name': 'ListaRps', 'type': 'ListaRpsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, NumeroLote=None, Cnpj=None, InscricaoMunicipal=None, QuantidadeRps=None, ListaRps=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.NumeroLote = NumeroLote
        self.validate_tsNumeroLote(self.NumeroLote)
        self.NumeroLote_nsprefix_ = None
        self.Cnpj = Cnpj
        self.validate_tsCnpj(self.Cnpj)
        self.Cnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        self.InscricaoMunicipal_nsprefix_ = None
        self.QuantidadeRps = QuantidadeRps
        self.validate_tsQuantidadeRps(self.QuantidadeRps)
        self.QuantidadeRps_nsprefix_ = None
        self.ListaRps = ListaRps
        self.ListaRps_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcLoteRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcLoteRps.subclass:
            return tcLoteRps.subclass(*args_, **kwargs_)
        else:
            return tcLoteRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tsNumeroLote(self, value):
        result = True
        # Validate type tsNumeroLote, a restriction on xsd:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsNumeroLote' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsCnpj(self, value):
        result = True
        # Validate type tsCnpj, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tsCnpj' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsInscricaoMunicipal(self, value):
        result = True
        # Validate type tsInscricaoMunicipal, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tsInscricaoMunicipal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tsQuantidadeRps(self, value):
        result = True
        # Validate type tsQuantidadeRps, a restriction on xsd:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tsQuantidadeRps' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tsIdTag(self, value):
        # Validate type tsIdTag, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tsIdTag' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.NumeroLote is not None or
            self.Cnpj is not None or
            self.InscricaoMunicipal is not None or
            self.QuantidadeRps is not None or
            self.ListaRps is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcLoteRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcLoteRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcLoteRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcLoteRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcLoteRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcLoteRps'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tcLoteRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NumeroLote is not None:
            namespaceprefix_ = self.NumeroLote_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroLote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroLote>%s</%sNumeroLote>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroLote, input_name='NumeroLote'), namespaceprefix_ , eol_))
        if self.Cnpj is not None:
            namespaceprefix_ = self.Cnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnpj_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnpj>%s</%sCnpj>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cnpj), input_name='Cnpj')), namespaceprefix_ , eol_))
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
        if self.QuantidadeRps is not None:
            namespaceprefix_ = self.QuantidadeRps_nsprefix_ + ':' if (UseCapturedNS_ and self.QuantidadeRps_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQuantidadeRps>%s</%sQuantidadeRps>%s' % (namespaceprefix_ , self.gds_format_integer(self.QuantidadeRps, input_name='QuantidadeRps'), namespaceprefix_ , eol_))
        if self.ListaRps is not None:
            namespaceprefix_ = self.ListaRps_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaRps_nsprefix_) else ''
            self.ListaRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaRps', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_tsIdTag(self.Id)    # validate type tsIdTag
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NumeroLote' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroLote')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroLote')
            self.NumeroLote = ival_
            self.NumeroLote_nsprefix_ = child_.prefix
            # validate type tsNumeroLote
            self.validate_tsNumeroLote(self.NumeroLote)
        elif nodeName_ == 'Cnpj':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnpj')
            value_ = self.gds_validate_string(value_, node, 'Cnpj')
            self.Cnpj = value_
            self.Cnpj_nsprefix_ = child_.prefix
            # validate type tsCnpj
            self.validate_tsCnpj(self.Cnpj)
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
            # validate type tsInscricaoMunicipal
            self.validate_tsInscricaoMunicipal(self.InscricaoMunicipal)
        elif nodeName_ == 'QuantidadeRps' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'QuantidadeRps')
            ival_ = self.gds_validate_integer(ival_, node, 'QuantidadeRps')
            self.QuantidadeRps = ival_
            self.QuantidadeRps_nsprefix_ = child_.prefix
            # validate type tsQuantidadeRps
            self.validate_tsQuantidadeRps(self.QuantidadeRps)
        elif nodeName_ == 'ListaRps':
            obj_ = ListaRpsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaRps = obj_
            obj_.original_tagname_ = 'ListaRps'
# end class tcLoteRps


class SignatureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('SignedInfo', 'SignedInfoType', 0, 0, {'name': 'SignedInfo', 'ref': 'SignedInfo', 'type': 'SignedInfo'}, None),
        MemberSpec_('SignatureValue', 'SignatureValueType', 0, 0, {'name': 'SignatureValue', 'ref': 'SignatureValue', 'type': 'SignatureValue'}, None),
        MemberSpec_('KeyInfo', 'KeyInfoType', 0, 1, {'minOccurs': '0', 'name': 'KeyInfo', 'ref': 'KeyInfo', 'type': 'KeyInfo'}, None),
        MemberSpec_('Object', 'ObjectType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Object', 'ref': 'Object', 'type': 'Object'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SignedInfo = SignedInfo
        self.SignedInfo_nsprefix_ = None
        self.SignatureValue = SignatureValue
        self.SignatureValue_nsprefix_ = None
        self.KeyInfo = KeyInfo
        self.KeyInfo_nsprefix_ = None
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
        self.Object_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureType.subclass:
            return SignatureType.subclass(*args_, **kwargs_)
        else:
            return SignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.SignedInfo is not None or
            self.SignatureValue is not None or
            self.KeyInfo is not None or
            self.Object
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SignedInfo is not None:
            namespaceprefix_ = self.SignedInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.SignedInfo_nsprefix_) else ''
            self.SignedInfo.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfo', pretty_print=pretty_print)
        if self.SignatureValue is not None:
            namespaceprefix_ = self.SignatureValue_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureValue_nsprefix_) else ''
            self.SignatureValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValue', pretty_print=pretty_print)
        if self.KeyInfo is not None:
            namespaceprefix_ = self.KeyInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyInfo_nsprefix_) else ''
            self.KeyInfo.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfo', pretty_print=pretty_print)
        for Object_ in self.Object:
            namespaceprefix_ = self.Object_nsprefix_ + ':' if (UseCapturedNS_ and self.Object_nsprefix_) else ''
            Object_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Object', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignedInfo':
            obj_ = SignedInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignedInfo = obj_
            obj_.original_tagname_ = 'SignedInfo'
        elif nodeName_ == 'SignatureValue':
            obj_ = SignatureValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureValue = obj_
            obj_.original_tagname_ = 'SignatureValue'
        elif nodeName_ == 'KeyInfo':
            obj_ = KeyInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyInfo = obj_
            obj_.original_tagname_ = 'KeyInfo'
        elif nodeName_ == 'Object':
            obj_ = ObjectType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Object.append(obj_)
            obj_.original_tagname_ = 'Object'
# end class SignatureType


class SignatureValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('valueOf_', 'base64Binary', 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureValueType.subclass:
            return SignatureValueType.subclass(*args_, **kwargs_)
        else:
            return SignatureValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureValueType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureValueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureValueType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureValueType


class SignedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('CanonicalizationMethod', 'CanonicalizationMethodType', 0, 0, {'name': 'CanonicalizationMethod', 'ref': 'CanonicalizationMethod', 'type': 'CanonicalizationMethod'}, None),
        MemberSpec_('SignatureMethod', 'SignatureMethodType', 0, 0, {'name': 'SignatureMethod', 'ref': 'SignatureMethod', 'type': 'SignatureMethod'}, None),
        MemberSpec_('Reference', 'ReferenceType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'Reference', 'ref': 'Reference', 'type': 'Reference'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.CanonicalizationMethod = CanonicalizationMethod
        self.CanonicalizationMethod_nsprefix_ = None
        self.SignatureMethod = SignatureMethod
        self.SignatureMethod_nsprefix_ = None
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignedInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignedInfoType.subclass:
            return SignedInfoType.subclass(*args_, **kwargs_)
        else:
            return SignedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.CanonicalizationMethod is not None or
            self.SignatureMethod is not None or
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignedInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignedInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignedInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CanonicalizationMethod is not None:
            namespaceprefix_ = self.CanonicalizationMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.CanonicalizationMethod_nsprefix_) else ''
            self.CanonicalizationMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='CanonicalizationMethod', pretty_print=pretty_print)
        if self.SignatureMethod is not None:
            namespaceprefix_ = self.SignatureMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureMethod_nsprefix_) else ''
            self.SignatureMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureMethod', pretty_print=pretty_print)
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CanonicalizationMethod':
            obj_ = CanonicalizationMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CanonicalizationMethod = obj_
            obj_.original_tagname_ = 'CanonicalizationMethod'
        elif nodeName_ == 'SignatureMethod':
            obj_ = SignatureMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureMethod = obj_
            obj_.original_tagname_ = 'SignatureMethod'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class SignedInfoType


class CanonicalizationMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
        MemberSpec_('__ANY__', '__ANY__', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'namespace': '##any'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CanonicalizationMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CanonicalizationMethodType.subclass:
            return CanonicalizationMethodType.subclass(*args_, **kwargs_)
        else:
            return CanonicalizationMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='CanonicalizationMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CanonicalizationMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CanonicalizationMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CanonicalizationMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CanonicalizationMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class CanonicalizationMethodType


class SignatureMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
        MemberSpec_('HMACOutputLength', ['HMACOutputLengthType', 'integer'], 0, 1, {'minOccurs': '0', 'name': 'HMACOutputLength', 'type': 'xsd:integer'}, None),
        MemberSpec_('__ANY__', '__ANY__', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'namespace': '##other'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        self.HMACOutputLength = HMACOutputLength
        self.validate_HMACOutputLengthType(self.HMACOutputLength)
        self.HMACOutputLength_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureMethodType.subclass:
            return SignatureMethodType.subclass(*args_, **kwargs_)
        else:
            return SignatureMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_HMACOutputLengthType(self, value):
        result = True
        # Validate type HMACOutputLengthType, a restriction on integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.HMACOutputLength is not None or
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HMACOutputLength is not None:
            namespaceprefix_ = self.HMACOutputLength_nsprefix_ + ':' if (UseCapturedNS_ and self.HMACOutputLength_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHMACOutputLength>%s</%sHMACOutputLength>%s' % (namespaceprefix_ , self.gds_format_integer(self.HMACOutputLength, input_name='HMACOutputLength'), namespaceprefix_ , eol_))
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'HMACOutputLength' and child_.text is not None:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'HMACOutputLength')
            ival_ = self.gds_validate_integer(ival_, node, 'HMACOutputLength')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeInteger, 'HMACOutputLength', ival_)
            self.content_.append(obj_)
            self.HMACOutputLength_nsprefix_ = child_.prefix
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SignatureMethodType


class ReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('URI', 'anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Type', 'anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Transforms', 'TransformsType', 0, 1, {'minOccurs': '0', 'name': 'Transforms', 'ref': 'Transforms', 'type': 'Transforms'}, None),
        MemberSpec_('DigestMethod', 'DigestMethodType', 0, 0, {'name': 'DigestMethod', 'ref': 'DigestMethod', 'type': 'DigestMethod'}, None),
        MemberSpec_('DigestValue', 'DigestValueType1', 0, 0, {'name': 'DigestValue', 'ref': 'DigestValue', 'type': 'DigestValue'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = None
        self.DigestMethod = DigestMethod
        self.DigestMethod_nsprefix_ = None
        self.DigestValue = DigestValue
        self.DigestValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Transforms is not None or
            self.DigestMethod is not None or
            self.DigestValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ReferenceType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transforms', pretty_print=pretty_print)
        if self.DigestMethod is not None:
            namespaceprefix_ = self.DigestMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestMethod_nsprefix_) else ''
            self.DigestMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestMethod', pretty_print=pretty_print)
        if self.DigestValue is not None:
            namespaceprefix_ = self.DigestValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestValue_nsprefix_) else ''
            self.DigestValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestValue', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
        elif nodeName_ == 'DigestMethod':
            obj_ = DigestMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestMethod = obj_
            obj_.original_tagname_ = 'DigestMethod'
        elif nodeName_ == 'DigestValue':
            obj_ = DigestValueType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestValue = obj_
            obj_.original_tagname_ = 'DigestValue'
# end class ReferenceType


class TransformsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Transform', 'TransformType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'Transform', 'ref': 'Transform', 'type': 'Transform'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Transform=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Transform is None:
            self.Transform = []
        else:
            self.Transform = Transform
        self.Transform_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformsType.subclass:
            return TransformsType.subclass(*args_, **kwargs_)
        else:
            return TransformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Transform
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transform_ in self.Transform:
            namespaceprefix_ = self.Transform_nsprefix_ + ':' if (UseCapturedNS_ and self.Transform_nsprefix_) else ''
            Transform_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transform', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType


class TransformType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
        MemberSpec_('__ANY__', '__ANY__', 0, 0, {'namespace': '##other', 'processContents': 'lax'}, None),
        MemberSpec_('XPath', 'xsd:string', 1, 1, {'name': 'XPath', 'type': 'xsd:string'}, 3),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        if XPath is None:
            self.XPath = []
        else:
            self.XPath = XPath
        self.XPath_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformType.subclass:
            return TransformType.subclass(*args_, **kwargs_)
        else:
            return TransformType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.anytypeobjs_ is not None or
            self.XPath or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for XPath_ in self.XPath:
            namespaceprefix_ = self.XPath_nsprefix_ + ':' if (UseCapturedNS_ and self.XPath_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sXPath>%s</%sXPath>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(XPath_), input_name='XPath')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        elif nodeName_ == 'XPath' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'XPath')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'XPath')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'XPath', valuestr_)
            self.content_.append(obj_)
            self.XPath_nsprefix_ = child_.prefix
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class TransformType


class DigestMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
        MemberSpec_('__ANY__', '__ANY__', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'namespace': '##other', 'processContents': 'lax'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestMethodType.subclass:
            return DigestMethodType.subclass(*args_, **kwargs_)
        else:
            return DigestMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class DigestMethodType


class KeyInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('KeyName', 'xsd:string', 1, 0, {'name': 'KeyName', 'ref': 'KeyName', 'type': 'KeyName'}, 4),
        MemberSpec_('KeyValue', 'KeyValueType', 1, 0, {'name': 'KeyValue', 'ref': 'KeyValue', 'type': 'KeyValue'}, 4),
        MemberSpec_('RetrievalMethod', 'RetrievalMethodType', 1, 0, {'name': 'RetrievalMethod', 'ref': 'RetrievalMethod', 'type': 'RetrievalMethod'}, 4),
        MemberSpec_('X509Data', 'X509DataType', 1, 0, {'name': 'X509Data', 'ref': 'X509Data', 'type': 'X509Data'}, 4),
        MemberSpec_('PGPData', 'PGPDataType', 1, 0, {'name': 'PGPData', 'ref': 'PGPData', 'type': 'PGPData'}, 4),
        MemberSpec_('SPKIData', 'SPKIDataType', 1, 0, {'name': 'SPKIData', 'ref': 'SPKIData', 'type': 'SPKIData'}, 4),
        MemberSpec_('MgmtData', 'xsd:string', 1, 0, {'name': 'MgmtData', 'ref': 'MgmtData', 'type': 'MgmtData'}, 4),
        MemberSpec_('__ANY__', '__ANY__', 0, 0, {'namespace': '##other', 'processContents': 'lax'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if KeyName is None:
            self.KeyName = []
        else:
            self.KeyName = KeyName
        self.KeyName_nsprefix_ = None
        if KeyValue is None:
            self.KeyValue = []
        else:
            self.KeyValue = KeyValue
        self.KeyValue_nsprefix_ = None
        if RetrievalMethod is None:
            self.RetrievalMethod = []
        else:
            self.RetrievalMethod = RetrievalMethod
        self.RetrievalMethod_nsprefix_ = None
        if X509Data is None:
            self.X509Data = []
        else:
            self.X509Data = X509Data
        self.X509Data_nsprefix_ = None
        if PGPData is None:
            self.PGPData = []
        else:
            self.PGPData = PGPData
        self.PGPData_nsprefix_ = None
        if SPKIData is None:
            self.SPKIData = []
        else:
            self.SPKIData = SPKIData
        self.SPKIData_nsprefix_ = None
        if MgmtData is None:
            self.MgmtData = []
        else:
            self.MgmtData = MgmtData
        self.MgmtData_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyInfoType.subclass:
            return KeyInfoType.subclass(*args_, **kwargs_)
        else:
            return KeyInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.KeyName or
            self.KeyValue or
            self.RetrievalMethod or
            self.X509Data or
            self.PGPData or
            self.SPKIData or
            self.MgmtData or
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for KeyName_ in self.KeyName:
            namespaceprefix_ = self.KeyName_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sKeyName>%s</%sKeyName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(KeyName_), input_name='KeyName')), namespaceprefix_ , eol_))
        for KeyValue_ in self.KeyValue:
            namespaceprefix_ = self.KeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyValue_nsprefix_) else ''
            KeyValue_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValue', pretty_print=pretty_print)
        for RetrievalMethod_ in self.RetrievalMethod:
            namespaceprefix_ = self.RetrievalMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.RetrievalMethod_nsprefix_) else ''
            RetrievalMethod_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RetrievalMethod', pretty_print=pretty_print)
        for X509Data_ in self.X509Data:
            namespaceprefix_ = self.X509Data_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Data_nsprefix_) else ''
            X509Data_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509Data', pretty_print=pretty_print)
        for PGPData_ in self.PGPData:
            namespaceprefix_ = self.PGPData_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPData_nsprefix_) else ''
            PGPData_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='PGPData', pretty_print=pretty_print)
        for SPKIData_ in self.SPKIData:
            namespaceprefix_ = self.SPKIData_nsprefix_ + ':' if (UseCapturedNS_ and self.SPKIData_nsprefix_) else ''
            SPKIData_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SPKIData', pretty_print=pretty_print)
        for MgmtData_ in self.MgmtData:
            namespaceprefix_ = self.MgmtData_nsprefix_ + ':' if (UseCapturedNS_ and self.MgmtData_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMgmtData>%s</%sMgmtData>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(MgmtData_), input_name='MgmtData')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KeyName' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'KeyName')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'KeyName')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'KeyName', valuestr_)
            self.content_.append(obj_)
            self.KeyName_nsprefix_ = child_.prefix
        elif nodeName_ == 'KeyValue':
            obj_ = KeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'KeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_KeyValue'):
              self.add_KeyValue(obj_.value)
            elif hasattr(self, 'set_KeyValue'):
              self.set_KeyValue(obj_.value)
        elif nodeName_ == 'RetrievalMethod':
            obj_ = RetrievalMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RetrievalMethod', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RetrievalMethod'):
              self.add_RetrievalMethod(obj_.value)
            elif hasattr(self, 'set_RetrievalMethod'):
              self.set_RetrievalMethod(obj_.value)
        elif nodeName_ == 'X509Data':
            obj_ = X509DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'X509Data', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_X509Data'):
              self.add_X509Data(obj_.value)
            elif hasattr(self, 'set_X509Data'):
              self.set_X509Data(obj_.value)
        elif nodeName_ == 'PGPData':
            obj_ = PGPDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'PGPData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_PGPData'):
              self.add_PGPData(obj_.value)
            elif hasattr(self, 'set_PGPData'):
              self.set_PGPData(obj_.value)
        elif nodeName_ == 'SPKIData':
            obj_ = SPKIDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SPKIData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SPKIData'):
              self.add_SPKIData(obj_.value)
            elif hasattr(self, 'set_SPKIData'):
              self.set_SPKIData(obj_.value)
        elif nodeName_ == 'MgmtData' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'MgmtData')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'MgmtData')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'MgmtData', valuestr_)
            self.content_.append(obj_)
            self.MgmtData_nsprefix_ = child_.prefix
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class KeyInfoType


class KeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('DSAKeyValue', 'DSAKeyValueType', 0, 0, {'name': 'DSAKeyValue', 'ref': 'DSAKeyValue', 'type': 'DSAKeyValue'}, 5),
        MemberSpec_('RSAKeyValue', 'RSAKeyValueType', 0, 0, {'name': 'RSAKeyValue', 'ref': 'RSAKeyValue', 'type': 'RSAKeyValue'}, 5),
        MemberSpec_('__ANY__', '__ANY__', 0, 0, {'namespace': '##other', 'processContents': 'lax'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.DSAKeyValue = DSAKeyValue
        self.DSAKeyValue_nsprefix_ = None
        self.RSAKeyValue = RSAKeyValue
        self.RSAKeyValue_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyValueType.subclass:
            return KeyValueType.subclass(*args_, **kwargs_)
        else:
            return KeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.DSAKeyValue is not None or
            self.RSAKeyValue is not None or
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValueType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DSAKeyValue is not None:
            namespaceprefix_ = self.DSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DSAKeyValue_nsprefix_) else ''
            self.DSAKeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DSAKeyValue', pretty_print=pretty_print)
        if self.RSAKeyValue is not None:
            namespaceprefix_ = self.RSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.RSAKeyValue_nsprefix_) else ''
            self.RSAKeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RSAKeyValue', pretty_print=pretty_print)
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DSAKeyValue':
            obj_ = DSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DSAKeyValue'):
              self.add_DSAKeyValue(obj_.value)
            elif hasattr(self, 'set_DSAKeyValue'):
              self.set_DSAKeyValue(obj_.value)
        elif nodeName_ == 'RSAKeyValue':
            obj_ = RSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RSAKeyValue'):
              self.add_RSAKeyValue(obj_.value)
            elif hasattr(self, 'set_RSAKeyValue'):
              self.set_RSAKeyValue(obj_.value)
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class KeyValueType


class RetrievalMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('URI', 'anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Type', 'anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Transforms', 'TransformsType', 0, 1, {'minOccurs': '0', 'name': 'Transforms', 'ref': 'Transforms', 'type': 'Transforms'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, URI=None, Type=None, Transforms=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetrievalMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetrievalMethodType.subclass:
            return RetrievalMethodType.subclass(*args_, **kwargs_)
        else:
            return RetrievalMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Transforms is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RetrievalMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetrievalMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetrievalMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetrievalMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetrievalMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='RetrievalMethodType'):
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RetrievalMethodType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transforms', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
# end class RetrievalMethodType


class X509DataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('X509IssuerSerial', 'X509IssuerSerialType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'X509IssuerSerial', 'type': 'X509IssuerSerialType'}, 6),
        MemberSpec_('X509SKI', 'xsd:string', 1, 0, {'maxOccurs': 'unbounded', 'name': 'X509SKI', 'type': 'xsd:string'}, 6),
        MemberSpec_('X509SubjectName', 'xsd:string', 1, 0, {'maxOccurs': 'unbounded', 'name': 'X509SubjectName', 'type': 'xsd:string'}, 6),
        MemberSpec_('X509Certificate', 'xsd:string', 1, 0, {'maxOccurs': 'unbounded', 'name': 'X509Certificate', 'type': 'xsd:string'}, 6),
        MemberSpec_('X509CRL', 'xsd:string', 1, 0, {'maxOccurs': 'unbounded', 'name': 'X509CRL', 'type': 'xsd:string'}, 6),
        MemberSpec_('__ANY__', '__ANY__', 0, 0, {'namespace': '##other', 'processContents': 'lax'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if X509IssuerSerial is None:
            self.X509IssuerSerial = []
        else:
            self.X509IssuerSerial = X509IssuerSerial
        self.X509IssuerSerial_nsprefix_ = None
        if X509SKI is None:
            self.X509SKI = []
        else:
            self.X509SKI = X509SKI
        self.X509SKI_nsprefix_ = None
        if X509SubjectName is None:
            self.X509SubjectName = []
        else:
            self.X509SubjectName = X509SubjectName
        self.X509SubjectName_nsprefix_ = None
        if X509Certificate is None:
            self.X509Certificate = []
        else:
            self.X509Certificate = X509Certificate
        self.X509Certificate_nsprefix_ = None
        if X509CRL is None:
            self.X509CRL = []
        else:
            self.X509CRL = X509CRL
        self.X509CRL_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509DataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509DataType.subclass:
            return X509DataType.subclass(*args_, **kwargs_)
        else:
            return X509DataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.X509IssuerSerial or
            self.X509SKI or
            self.X509SubjectName or
            self.X509Certificate or
            self.X509CRL or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509DataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509DataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509DataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509DataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for X509IssuerSerial_ in self.X509IssuerSerial:
            namespaceprefix_ = self.X509IssuerSerial_nsprefix_ + ':' if (UseCapturedNS_ and self.X509IssuerSerial_nsprefix_) else ''
            X509IssuerSerial_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='X509IssuerSerial', pretty_print=pretty_print)
        for X509SKI_ in self.X509SKI:
            namespaceprefix_ = self.X509SKI_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SKI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SKI>%s</%sX509SKI>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509SKI_), input_name='X509SKI')), namespaceprefix_ , eol_))
        for X509SubjectName_ in self.X509SubjectName:
            namespaceprefix_ = self.X509SubjectName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SubjectName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SubjectName>%s</%sX509SubjectName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509SubjectName_), input_name='X509SubjectName')), namespaceprefix_ , eol_))
        for X509Certificate_ in self.X509Certificate:
            namespaceprefix_ = self.X509Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509Certificate>%s</%sX509Certificate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509Certificate_), input_name='X509Certificate')), namespaceprefix_ , eol_))
        for X509CRL_ in self.X509CRL:
            namespaceprefix_ = self.X509CRL_nsprefix_ + ':' if (UseCapturedNS_ and self.X509CRL_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509CRL>%s</%sX509CRL>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509CRL_), input_name='X509CRL')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509IssuerSerial':
            obj_ = X509IssuerSerialType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.X509IssuerSerial.append(obj_)
            obj_.original_tagname_ = 'X509IssuerSerial'
        elif nodeName_ == 'X509SKI':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SKI')
            value_ = self.gds_validate_string(value_, node, 'X509SKI')
            self.X509SKI.append(value_)
            self.X509SKI_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SubjectName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SubjectName')
            value_ = self.gds_validate_string(value_, node, 'X509SubjectName')
            self.X509SubjectName.append(value_)
            self.X509SubjectName_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509Certificate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509Certificate')
            value_ = self.gds_validate_string(value_, node, 'X509Certificate')
            self.X509Certificate.append(value_)
            self.X509Certificate_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509CRL':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509CRL')
            value_ = self.gds_validate_string(value_, node, 'X509CRL')
            self.X509CRL.append(value_)
            self.X509CRL_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'X509DataType')
            self.set_anytypeobjs_(content_)
# end class X509DataType


class X509IssuerSerialType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('X509IssuerName', 'xsd:string', 0, 0, {'name': 'X509IssuerName', 'type': 'xsd:string'}, None),
        MemberSpec_('X509SerialNumber', 'xsd:string', 0, 0, {'name': 'X509SerialNumber', 'type': 'xsd:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, X509IssuerName=None, X509SerialNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.X509IssuerName = X509IssuerName
        self.X509IssuerName_nsprefix_ = None
        self.X509SerialNumber = X509SerialNumber
        self.X509SerialNumber_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509IssuerSerialType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509IssuerSerialType.subclass:
            return X509IssuerSerialType.subclass(*args_, **kwargs_)
        else:
            return X509IssuerSerialType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.X509IssuerName is not None or
            self.X509SerialNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509IssuerSerialType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509IssuerSerialType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509IssuerSerialType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509IssuerSerialType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509IssuerSerialType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509IssuerSerialType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509IssuerSerialType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509IssuerName is not None:
            namespaceprefix_ = self.X509IssuerName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509IssuerName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509IssuerName>%s</%sX509IssuerName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509IssuerName), input_name='X509IssuerName')), namespaceprefix_ , eol_))
        if self.X509SerialNumber is not None:
            namespaceprefix_ = self.X509SerialNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SerialNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SerialNumber>%s</%sX509SerialNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509SerialNumber), input_name='X509SerialNumber')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509IssuerName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509IssuerName')
            value_ = self.gds_validate_string(value_, node, 'X509IssuerName')
            self.X509IssuerName = value_
            self.X509IssuerName_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SerialNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SerialNumber')
            value_ = self.gds_validate_string(value_, node, 'X509SerialNumber')
            self.X509SerialNumber = value_
            self.X509SerialNumber_nsprefix_ = child_.prefix
# end class X509IssuerSerialType


class PGPDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('PGPKeyID', 'xsd:string', 0, 0, {'name': 'PGPKeyID', 'type': 'xsd:string'}, 7),
        MemberSpec_('PGPKeyPacket', 'xsd:string', 0, 0, {'name': 'PGPKeyPacket', 'type': 'xsd:string'}, 7),
        MemberSpec_('__ANY__', '__ANY__', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'namespace': '##other', 'processContents': 'lax'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.PGPKeyID = PGPKeyID
        self.PGPKeyID_nsprefix_ = None
        self.PGPKeyPacket = PGPKeyPacket
        self.PGPKeyPacket_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PGPDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PGPDataType.subclass:
            return PGPDataType.subclass(*args_, **kwargs_)
        else:
            return PGPDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.PGPKeyID is not None or
            self.PGPKeyPacket is not None or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='PGPDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PGPDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PGPDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PGPDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PGPDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='PGPDataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='PGPDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PGPKeyID is not None:
            namespaceprefix_ = self.PGPKeyID_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPKeyID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPGPKeyID>%s</%sPGPKeyID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PGPKeyID), input_name='PGPKeyID')), namespaceprefix_ , eol_))
        if self.PGPKeyPacket is not None:
            namespaceprefix_ = self.PGPKeyPacket_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPKeyPacket_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPGPKeyPacket>%s</%sPGPKeyPacket>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PGPKeyPacket), input_name='PGPKeyPacket')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PGPKeyID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PGPKeyID')
            value_ = self.gds_validate_string(value_, node, 'PGPKeyID')
            self.PGPKeyID = value_
            self.PGPKeyID_nsprefix_ = child_.prefix
        elif nodeName_ == 'PGPKeyPacket':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PGPKeyPacket')
            value_ = self.gds_validate_string(value_, node, 'PGPKeyPacket')
            self.PGPKeyPacket = value_
            self.PGPKeyPacket_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'PGPDataType')
            self.add_anytypeobjs_(content_)
# end class PGPDataType


class SPKIDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('SPKISexp', 'xsd:string', 1, 0, {'maxOccurs': 'unbounded', 'name': 'SPKISexp', 'type': 'xsd:string'}, None),
        MemberSpec_('__ANY__', '__ANY__', 0, 1, {'minOccurs': '0', 'namespace': '##other', 'processContents': 'lax'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, SPKISexp=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if SPKISexp is None:
            self.SPKISexp = []
        else:
            self.SPKISexp = SPKISexp
        self.SPKISexp_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SPKIDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SPKIDataType.subclass:
            return SPKIDataType.subclass(*args_, **kwargs_)
        else:
            return SPKIDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.SPKISexp or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SPKIDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SPKIDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SPKIDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SPKIDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SPKIDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SPKIDataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SPKIDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SPKISexp_ in self.SPKISexp:
            namespaceprefix_ = self.SPKISexp_nsprefix_ + ':' if (UseCapturedNS_ and self.SPKISexp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSPKISexp>%s</%sSPKISexp>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(SPKISexp_), input_name='SPKISexp')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SPKISexp':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SPKISexp')
            value_ = self.gds_validate_string(value_, node, 'SPKISexp')
            self.SPKISexp.append(value_)
            self.SPKISexp_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'SPKIDataType')
            self.set_anytypeobjs_(content_)
# end class SPKIDataType


class ObjectType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('MimeType', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('Encoding', 'anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('__ANY__', '__ANY__', 0, 0, {'namespace': '##any', 'processContents': 'lax'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, MimeType=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.MimeType = _cast(None, MimeType)
        self.MimeType_nsprefix_ = None
        self.Encoding = _cast(None, Encoding)
        self.Encoding_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectType.subclass:
            return ObjectType.subclass(*args_, **kwargs_)
        else:
            return ObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ObjectType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ObjectType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.MimeType is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            outfile.write(' MimeType=%s' % (quote_attrib(self.MimeType), ))
        if self.Encoding is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            outfile.write(' Encoding=%s' % (quote_attrib(self.Encoding), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ObjectType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('MimeType', node)
        if value is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            self.MimeType = value
        value = find_attr_value_('Encoding', node)
        if value is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            self.Encoding = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class ObjectType


class ManifestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('Reference', 'ReferenceType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'Reference', 'ref': 'Reference', 'type': 'Reference'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestType.subclass:
            return ManifestType.subclass(*args_, **kwargs_)
        else:
            return ManifestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ManifestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ManifestType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ManifestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class ManifestType


class SignaturePropertiesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('SignatureProperty', 'SignaturePropertyType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'SignatureProperty', 'ref': 'SignatureProperty', 'type': 'SignatureProperty'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignatureProperty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if SignatureProperty is None:
            self.SignatureProperty = []
        else:
            self.SignatureProperty = SignatureProperty
        self.SignatureProperty_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignaturePropertiesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignaturePropertiesType.subclass:
            return SignaturePropertiesType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.SignatureProperty
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignaturePropertiesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignaturePropertiesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignaturePropertiesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignaturePropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignaturePropertiesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignaturePropertiesType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignaturePropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SignatureProperty_ in self.SignatureProperty:
            namespaceprefix_ = self.SignatureProperty_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureProperty_nsprefix_) else ''
            SignatureProperty_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureProperty', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignatureProperty':
            obj_ = SignaturePropertyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureProperty.append(obj_)
            obj_.original_tagname_ = 'SignatureProperty'
# end class SignaturePropertiesType


class SignaturePropertyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Target', 'anyURI', 0, 0, {'use': 'required'}),
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('__ANY__', '__ANY__', 0, 0, {'namespace': '##other', 'processContents': 'lax'}, None),
        MemberSpec_('valueOf_', [], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Target = _cast(None, Target)
        self.Target_nsprefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignaturePropertyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignaturePropertyType.subclass:
            return SignaturePropertyType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignaturePropertyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignaturePropertyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignaturePropertyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignaturePropertyType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignaturePropertyType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignaturePropertyType'):
        if self.Target is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            outfile.write(' Target=%s' % (quote_attrib(self.Target), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignaturePropertyType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Target', node)
        if value is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            self.Target = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SignaturePropertyType


class DSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('P', ['CryptoBinary', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'P', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('Q', ['CryptoBinary', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'Q', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('G', ['CryptoBinary', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'G', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('Y', ['CryptoBinary', 'base64Binary'], 0, 0, {'name': 'Y', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('J', ['CryptoBinary', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'J', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('Seed', ['CryptoBinary', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'Seed', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('PgenCounter', ['CryptoBinary', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'PgenCounter', 'type': 'xsd:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.P = P
        self.validate_CryptoBinary(self.P)
        self.P_nsprefix_ = None
        self.Q = Q
        self.validate_CryptoBinary(self.Q)
        self.Q_nsprefix_ = None
        self.G = G
        self.validate_CryptoBinary(self.G)
        self.G_nsprefix_ = None
        self.Y = Y
        self.validate_CryptoBinary(self.Y)
        self.Y_nsprefix_ = None
        self.J = J
        self.validate_CryptoBinary(self.J)
        self.J_nsprefix_ = None
        self.Seed = Seed
        self.validate_CryptoBinary(self.Seed)
        self.Seed_nsprefix_ = None
        self.PgenCounter = PgenCounter
        self.validate_CryptoBinary(self.PgenCounter)
        self.PgenCounter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DSAKeyValueType.subclass:
            return DSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return DSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def hasContent_(self):
        if (
            self.P is not None or
            self.Q is not None or
            self.G is not None or
            self.Y is not None or
            self.J is not None or
            self.Seed is not None or
            self.PgenCounter is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DSAKeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='DSAKeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.P is not None:
            namespaceprefix_ = self.P_nsprefix_ + ':' if (UseCapturedNS_ and self.P_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sP>%s</%sP>%s' % (namespaceprefix_ , self.gds_format_base64(self.P, input_name='P'), namespaceprefix_ , eol_))
        if self.Q is not None:
            namespaceprefix_ = self.Q_nsprefix_ + ':' if (UseCapturedNS_ and self.Q_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQ>%s</%sQ>%s' % (namespaceprefix_ , self.gds_format_base64(self.Q, input_name='Q'), namespaceprefix_ , eol_))
        if self.G is not None:
            namespaceprefix_ = self.G_nsprefix_ + ':' if (UseCapturedNS_ and self.G_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sG>%s</%sG>%s' % (namespaceprefix_ , self.gds_format_base64(self.G, input_name='G'), namespaceprefix_ , eol_))
        if self.Y is not None:
            namespaceprefix_ = self.Y_nsprefix_ + ':' if (UseCapturedNS_ and self.Y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sY>%s</%sY>%s' % (namespaceprefix_ , self.gds_format_base64(self.Y, input_name='Y'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_base64(self.J, input_name='J'), namespaceprefix_ , eol_))
        if self.Seed is not None:
            namespaceprefix_ = self.Seed_nsprefix_ + ':' if (UseCapturedNS_ and self.Seed_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSeed>%s</%sSeed>%s' % (namespaceprefix_ , self.gds_format_base64(self.Seed, input_name='Seed'), namespaceprefix_ , eol_))
        if self.PgenCounter is not None:
            namespaceprefix_ = self.PgenCounter_nsprefix_ + ':' if (UseCapturedNS_ and self.PgenCounter_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPgenCounter>%s</%sPgenCounter>%s' % (namespaceprefix_ , self.gds_format_base64(self.PgenCounter, input_name='PgenCounter'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'P':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'P')
            else:
                bval_ = None
            self.P = bval_
            self.P_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.P)
        elif nodeName_ == 'Q':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Q')
            else:
                bval_ = None
            self.Q = bval_
            self.Q_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Q)
        elif nodeName_ == 'G':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'G')
            else:
                bval_ = None
            self.G = bval_
            self.G_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.G)
        elif nodeName_ == 'Y':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Y')
            else:
                bval_ = None
            self.Y = bval_
            self.Y_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Y)
        elif nodeName_ == 'J':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'J')
            else:
                bval_ = None
            self.J = bval_
            self.J_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.J)
        elif nodeName_ == 'Seed':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Seed')
            else:
                bval_ = None
            self.Seed = bval_
            self.Seed_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Seed)
        elif nodeName_ == 'PgenCounter':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'PgenCounter')
            else:
                bval_ = None
            self.PgenCounter = bval_
            self.PgenCounter_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.PgenCounter)
# end class DSAKeyValueType


class RSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Modulus', ['CryptoBinary', 'base64Binary'], 0, 0, {'name': 'Modulus', 'type': 'xsd:base64Binary'}, None),
        MemberSpec_('Exponent', ['CryptoBinary', 'base64Binary'], 0, 0, {'name': 'Exponent', 'type': 'xsd:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Modulus=None, Exponent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Modulus = Modulus
        self.validate_CryptoBinary(self.Modulus)
        self.Modulus_nsprefix_ = None
        self.Exponent = Exponent
        self.validate_CryptoBinary(self.Exponent)
        self.Exponent_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RSAKeyValueType.subclass:
            return RSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return RSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def hasContent_(self):
        if (
            self.Modulus is not None or
            self.Exponent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RSAKeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='RSAKeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Modulus is not None:
            namespaceprefix_ = self.Modulus_nsprefix_ + ':' if (UseCapturedNS_ and self.Modulus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sModulus>%s</%sModulus>%s' % (namespaceprefix_ , self.gds_format_base64(self.Modulus, input_name='Modulus'), namespaceprefix_ , eol_))
        if self.Exponent is not None:
            namespaceprefix_ = self.Exponent_nsprefix_ + ':' if (UseCapturedNS_ and self.Exponent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExponent>%s</%sExponent>%s' % (namespaceprefix_ , self.gds_format_base64(self.Exponent, input_name='Exponent'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Modulus':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Modulus')
            else:
                bval_ = None
            self.Modulus = bval_
            self.Modulus_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Modulus)
        elif nodeName_ == 'Exponent':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Exponent')
            else:
                bval_ = None
            self.Exponent = bval_
            self.Exponent_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Exponent)
# end class RSAKeyValueType


class ListaNfseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CompNfse', 'tcCompNfse', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'CompNfse', 'type': 'tcCompNfse'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CompNfse=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if CompNfse is None:
            self.CompNfse = []
        else:
            self.CompNfse = CompNfse
        self.CompNfse_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaNfseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaNfseType.subclass:
            return ListaNfseType.subclass(*args_, **kwargs_)
        else:
            return ListaNfseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.CompNfse
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListaNfseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaNfseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaNfseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaNfseType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaNfseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaNfseType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListaNfseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for CompNfse_ in self.CompNfse:
            namespaceprefix_ = self.CompNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.CompNfse_nsprefix_) else ''
            CompNfse_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CompNfse', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CompNfse':
            obj_ = tcCompNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CompNfse.append(obj_)
            obj_.original_tagname_ = 'CompNfse'
# end class ListaNfseType


class ListaRpsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Rps', 'tcRps', 1, 0, {'maxOccurs': 'unbounded', 'name': 'Rps', 'type': 'tcRps'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Rps=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Rps is None:
            self.Rps = []
        else:
            self.Rps = Rps
        self.Rps_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaRpsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaRpsType.subclass:
            return ListaRpsType.subclass(*args_, **kwargs_)
        else:
            return ListaRpsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Rps
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListaRpsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaRpsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaRpsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaRpsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaRpsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaRpsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ListaRpsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Rps_ in self.Rps:
            namespaceprefix_ = self.Rps_nsprefix_ + ':' if (UseCapturedNS_ and self.Rps_nsprefix_) else ''
            Rps_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Rps', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Rps':
            obj_ = tcRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Rps.append(obj_)
            obj_.original_tagname_ = 'Rps'
# end class ListaRpsType


class DigestValueType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('valueOf_', ['DigestValueType', 'base64Binary'], 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestValueType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestValueType1.subclass:
            return DigestValueType1.subclass(*args_, **kwargs_)
        else:
            return DigestValueType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestValueType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestValueType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestValueType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestValueType1')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestValueType1', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigestValueType1'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestValueType1', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DigestValueType1


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ConsultarLoteRpsResposta'
        rootClass = ConsultarLoteRpsResposta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ConsultarLoteRpsResposta'
        rootClass = ConsultarLoteRpsResposta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ConsultarLoteRpsResposta'
        rootClass = ConsultarLoteRpsResposta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ConsultarLoteRpsResposta'
        rootClass = ConsultarLoteRpsResposta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from servico_consultar_lote_rps_resposta import *\n\n')
        sys.stdout.write('import servico_consultar_lote_rps_resposta as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.ginfes.com.br/servico_consultar_lote_rps_resposta_v03.xsd': [],
 'http://www.ginfes.com.br/tipos_v03.xsd': [('tsNumeroNfse',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoVerificacao',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsStatusRps',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsStatusNfse',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsNaturezaOperacao',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsRegimeEspecialTributacao',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsSimNao', 'tipos_v03.xsd', 'ST'),
                                            ('tsNumeroRps',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsSerieRps',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsTipoRps',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsOutrasInformacoes',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsValor', 'tipos_v03.xsd', 'ST'),
                                            ('tsItemListaServico',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoCnae',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoTributacao',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsAliquota',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsDiscriminacao',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoMunicipioIbge',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsInscricaoMunicipal',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsRazaoSocial',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsNomeFantasia',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCnpj', 'tipos_v03.xsd', 'ST'),
                                            ('tsEndereco',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsNumeroEndereco',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsComplementoEndereco',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsBairro', 'tipos_v03.xsd', 'ST'),
                                            ('tsUf', 'tipos_v03.xsd', 'ST'),
                                            ('tsCep', 'tipos_v03.xsd', 'ST'),
                                            ('tsEmail', 'tipos_v03.xsd', 'ST'),
                                            ('tsTelefone',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCpf', 'tipos_v03.xsd', 'ST'),
                                            ('tsIndicacaoCpfCnpj',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoObra',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsArt', 'tipos_v03.xsd', 'ST'),
                                            ('tsNumeroLote',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsNumeroProtocolo',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsSituacaoLoteRps',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsQuantidadeRps',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoMensagemAlerta',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsDescricaoMensagemAlerta',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsCodigoCancelamentoNfse',
                                             'tipos_v03.xsd',
                                             'ST'),
                                            ('tsIdTag', 'tipos_v03.xsd', 'ST'),
                                            ('tsVersao', 'tipos_v03.xsd', 'ST'),
                                            ('tcCpfCnpj',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcEndereco',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcContato',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcIdentificacaoOrgaoGerador',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcIdentificacaoRps',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcIdentificacaoPrestador',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcIdentificacaoTomador',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcDadosTomador',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcIdentificacaoIntermediarioServico',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcValores',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcDadosServico',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcDadosConstrucaoCivil',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcDadosPrestador',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcInfRps', 'tipos_v03.xsd', 'CT'),
                                            ('tcRps', 'tipos_v03.xsd', 'CT'),
                                            ('tcIdentificacaoNfse',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcInfNfse',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcNfse', 'tipos_v03.xsd', 'CT'),
                                            ('tcInfPedidoCancelamento',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcPedidoCancelamento',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcInfConfirmacaoCancelamento',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcConfirmacaoCancelamento',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcCancelamentoNfse',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcInfSubstituicaoNfse',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcSubstituicaoNfse',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcCompNfse',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcMensagemRetorno',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcMensagemRetornoLote',
                                             'tipos_v03.xsd',
                                             'CT'),
                                            ('tcLoteRps',
                                             'tipos_v03.xsd',
                                             'CT')],
 'http://www.w3.org/2000/09/xmldsig#': [('CryptoBinary',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'ST'),
                                        ('DigestValueType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'ST'),
                                        ('HMACOutputLengthType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'ST'),
                                        ('SignatureType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('SignatureValueType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('SignedInfoType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('CanonicalizationMethodType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('SignatureMethodType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('ReferenceType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('TransformsType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('TransformType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('DigestMethodType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('KeyInfoType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('KeyValueType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('RetrievalMethodType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('X509DataType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('X509IssuerSerialType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('PGPDataType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('SPKIDataType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('ObjectType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('ManifestType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('SignaturePropertiesType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('SignaturePropertyType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('DSAKeyValueType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT'),
                                        ('RSAKeyValueType',
                                         'xmldsig-core-schema20020212_v03.xsd',
                                         'CT')]}

__all__ = [
    "CanonicalizationMethodType",
    "ConsultarLoteRpsResposta",
    "DSAKeyValueType",
    "DigestMethodType",
    "DigestValueType1",
    "KeyInfoType",
    "KeyValueType",
    "ListaMensagemRetorno",
    "ListaNfseType",
    "ListaRpsType",
    "ManifestType",
    "ObjectType",
    "PGPDataType",
    "RSAKeyValueType",
    "ReferenceType",
    "RetrievalMethodType",
    "SPKIDataType",
    "SignatureMethodType",
    "SignaturePropertiesType",
    "SignaturePropertyType",
    "SignatureType",
    "SignatureValueType",
    "SignedInfoType",
    "TransformType",
    "TransformsType",
    "X509DataType",
    "X509IssuerSerialType",
    "tcCancelamentoNfse",
    "tcCompNfse",
    "tcConfirmacaoCancelamento",
    "tcContato",
    "tcCpfCnpj",
    "tcDadosConstrucaoCivil",
    "tcDadosPrestador",
    "tcDadosServico",
    "tcDadosTomador",
    "tcEndereco",
    "tcIdentificacaoIntermediarioServico",
    "tcIdentificacaoNfse",
    "tcIdentificacaoOrgaoGerador",
    "tcIdentificacaoPrestador",
    "tcIdentificacaoRps",
    "tcIdentificacaoTomador",
    "tcInfConfirmacaoCancelamento",
    "tcInfNfse",
    "tcInfPedidoCancelamento",
    "tcInfRps",
    "tcInfSubstituicaoNfse",
    "tcLoteRps",
    "tcMensagemRetorno",
    "tcMensagemRetornoLote",
    "tcNfse",
    "tcPedidoCancelamento",
    "tcRps",
    "tcSubstituicaoNfse",
    "tcValores"
]
