# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

__all__ = ['PassportElementError', 'PassportElementErrorDataField', 'PassportElementErrorFrontSide', 'PassportElementErrorReverseSide', 'PassportElementErrorSelfie', 'PassportElementErrorFile', 'PassportElementErrorFiles']
__author__ = 'luckydonald'


class PassportElementError(Sendable):
    """
    This object represents an error in the Telegram Passport element
    which was submitted that should be resolved by the user.
    """
    pass
# end class


class PassportElementErrorDataField(PassportElementError):
    """
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    https://core.telegram.org/bots/api#passportelementerrordatafield
    

    Parameters:
    
    :param source: Error source, must be data
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”
    :type  type: str|unicode
    
    :param field_name: Name of the data field which has the error
    :type  field_name: str|unicode
    
    :param data_hash: Base64-encoded data hash
    :type  data_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, source, type, field_name, data_hash, message):
        """
        Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
    
        https://core.telegram.org/bots/api#passportelementerrordatafield
        
    
        Parameters:
        
        :param source: Error source, must be data
        :type  source: str|unicode
        
        :param type: The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”
        :type  type: str|unicode
        
        :param field_name: Name of the data field which has the error
        :type  field_name: str|unicode
        
        :param data_hash: Base64-encoded data hash
        :type  data_hash: str|unicode
        
        :param message: Error message
        :type  message: str|unicode
        
    
        Optional keyword parameters:
        """
        super(PassportElementErrorDataField, self).__init__()
        assert_type_or_raise(source, unicode_type, parameter_name="source")
        self.source = source
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(field_name, unicode_type, parameter_name="field_name")
        self.field_name = field_name
        
        assert_type_or_raise(data_hash, unicode_type, parameter_name="data_hash")
        self.data_hash = data_hash
        
        assert_type_or_raise(message, unicode_type, parameter_name="message")
        self.message = message
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportElementErrorDataField to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportElementErrorDataField, self).to_array()
        array['source'] = u(self.source)  # py2: type unicode, py3: type str
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['field_name'] = u(self.field_name)  # py2: type unicode, py3: type str
        array['data_hash'] = u(self.data_hash)  # py2: type unicode, py3: type str
        array['message'] = u(self.message)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportElementErrorDataField from a given dictionary.

        :return: new PassportElementErrorDataField instance.
        :rtype: PassportElementErrorDataField
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['source'] = u(array.get('source'))
        data['type'] = u(array.get('type'))
        data['field_name'] = u(array.get('field_name'))
        data['data_hash'] = u(array.get('data_hash'))
        data['message'] = u(array.get('message'))
        
        instance = PassportElementErrorDataField(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportelementerrordatafield_instance)`
        """
        return "PassportElementErrorDataField(source={self.source!r}, type={self.type!r}, field_name={self.field_name!r}, data_hash={self.data_hash!r}, message={self.message!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportelementerrordatafield_instance)`
        """
        if self._raw:
            return "PassportElementErrorDataField.from_array({self._raw})".format(self=self)
        # end if
        return "PassportElementErrorDataField(source={self.source!r}, type={self.type!r}, field_name={self.field_name!r}, data_hash={self.data_hash!r}, message={self.message!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportelementerrordatafield_instance`
        """
        return key in ["source", "type", "field_name", "data_hash", "message"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class PassportElementErrorDataField



class PassportElementErrorFrontSide(PassportElementError):
    """
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorfrontside
    

    Parameters:
    
    :param source: Error source, must be front_side
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded hash of the file with the front side of the document
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, source, type, file_hash, message):
        """
        Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.
    
        https://core.telegram.org/bots/api#passportelementerrorfrontside
        
    
        Parameters:
        
        :param source: Error source, must be front_side
        :type  source: str|unicode
        
        :param type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
        :type  type: str|unicode
        
        :param file_hash: Base64-encoded hash of the file with the front side of the document
        :type  file_hash: str|unicode
        
        :param message: Error message
        :type  message: str|unicode
        
    
        Optional keyword parameters:
        """
        super(PassportElementErrorFrontSide, self).__init__()
        assert_type_or_raise(source, unicode_type, parameter_name="source")
        self.source = source
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(file_hash, unicode_type, parameter_name="file_hash")
        self.file_hash = file_hash
        
        assert_type_or_raise(message, unicode_type, parameter_name="message")
        self.message = message
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportElementErrorFrontSide to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportElementErrorFrontSide, self).to_array()
        array['source'] = u(self.source)  # py2: type unicode, py3: type str
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['file_hash'] = u(self.file_hash)  # py2: type unicode, py3: type str
        array['message'] = u(self.message)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportElementErrorFrontSide from a given dictionary.

        :return: new PassportElementErrorFrontSide instance.
        :rtype: PassportElementErrorFrontSide
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['source'] = u(array.get('source'))
        data['type'] = u(array.get('type'))
        data['file_hash'] = u(array.get('file_hash'))
        data['message'] = u(array.get('message'))
        
        instance = PassportElementErrorFrontSide(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportelementerrorfrontside_instance)`
        """
        return "PassportElementErrorFrontSide(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportelementerrorfrontside_instance)`
        """
        if self._raw:
            return "PassportElementErrorFrontSide.from_array({self._raw})".format(self=self)
        # end if
        return "PassportElementErrorFrontSide(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportelementerrorfrontside_instance`
        """
        return key in ["source", "type", "file_hash", "message"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class PassportElementErrorFrontSide



class PassportElementErrorReverseSide(PassportElementError):
    """
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorreverseside
    

    Parameters:
    
    :param source: Error source, must be reverse_side
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded hash of the file with the reverse side of the document
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, source, type, file_hash, message):
        """
        Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.
    
        https://core.telegram.org/bots/api#passportelementerrorreverseside
        
    
        Parameters:
        
        :param source: Error source, must be reverse_side
        :type  source: str|unicode
        
        :param type: The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”
        :type  type: str|unicode
        
        :param file_hash: Base64-encoded hash of the file with the reverse side of the document
        :type  file_hash: str|unicode
        
        :param message: Error message
        :type  message: str|unicode
        
    
        Optional keyword parameters:
        """
        super(PassportElementErrorReverseSide, self).__init__()
        assert_type_or_raise(source, unicode_type, parameter_name="source")
        self.source = source
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(file_hash, unicode_type, parameter_name="file_hash")
        self.file_hash = file_hash
        
        assert_type_or_raise(message, unicode_type, parameter_name="message")
        self.message = message
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportElementErrorReverseSide to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportElementErrorReverseSide, self).to_array()
        array['source'] = u(self.source)  # py2: type unicode, py3: type str
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['file_hash'] = u(self.file_hash)  # py2: type unicode, py3: type str
        array['message'] = u(self.message)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportElementErrorReverseSide from a given dictionary.

        :return: new PassportElementErrorReverseSide instance.
        :rtype: PassportElementErrorReverseSide
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['source'] = u(array.get('source'))
        data['type'] = u(array.get('type'))
        data['file_hash'] = u(array.get('file_hash'))
        data['message'] = u(array.get('message'))
        
        instance = PassportElementErrorReverseSide(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportelementerrorreverseside_instance)`
        """
        return "PassportElementErrorReverseSide(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportelementerrorreverseside_instance)`
        """
        if self._raw:
            return "PassportElementErrorReverseSide.from_array({self._raw})".format(self=self)
        # end if
        return "PassportElementErrorReverseSide(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportelementerrorreverseside_instance`
        """
        return key in ["source", "type", "file_hash", "message"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class PassportElementErrorReverseSide



class PassportElementErrorSelfie(PassportElementError):
    """
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    https://core.telegram.org/bots/api#passportelementerrorselfie
    

    Parameters:
    
    :param source: Error source, must be selfie
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded hash of the file with the selfie
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, source, type, file_hash, message):
        """
        Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.
    
        https://core.telegram.org/bots/api#passportelementerrorselfie
        
    
        Parameters:
        
        :param source: Error source, must be selfie
        :type  source: str|unicode
        
        :param type: The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”
        :type  type: str|unicode
        
        :param file_hash: Base64-encoded hash of the file with the selfie
        :type  file_hash: str|unicode
        
        :param message: Error message
        :type  message: str|unicode
        
    
        Optional keyword parameters:
        """
        super(PassportElementErrorSelfie, self).__init__()
        assert_type_or_raise(source, unicode_type, parameter_name="source")
        self.source = source
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(file_hash, unicode_type, parameter_name="file_hash")
        self.file_hash = file_hash
        
        assert_type_or_raise(message, unicode_type, parameter_name="message")
        self.message = message
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportElementErrorSelfie to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportElementErrorSelfie, self).to_array()
        array['source'] = u(self.source)  # py2: type unicode, py3: type str
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['file_hash'] = u(self.file_hash)  # py2: type unicode, py3: type str
        array['message'] = u(self.message)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportElementErrorSelfie from a given dictionary.

        :return: new PassportElementErrorSelfie instance.
        :rtype: PassportElementErrorSelfie
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['source'] = u(array.get('source'))
        data['type'] = u(array.get('type'))
        data['file_hash'] = u(array.get('file_hash'))
        data['message'] = u(array.get('message'))
        
        instance = PassportElementErrorSelfie(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportelementerrorselfie_instance)`
        """
        return "PassportElementErrorSelfie(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportelementerrorselfie_instance)`
        """
        if self._raw:
            return "PassportElementErrorSelfie.from_array({self._raw})".format(self=self)
        # end if
        return "PassportElementErrorSelfie(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportelementerrorselfie_instance`
        """
        return key in ["source", "type", "file_hash", "message"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class PassportElementErrorSelfie



class PassportElementErrorFile(PassportElementError):
    """
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    https://core.telegram.org/bots/api#passportelementerrorfile
    

    Parameters:
    
    :param source: Error source, must be file
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    :type  type: str|unicode
    
    :param file_hash: Base64-encoded file hash
    :type  file_hash: str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, source, type, file_hash, message):
        """
        Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.
    
        https://core.telegram.org/bots/api#passportelementerrorfile
        
    
        Parameters:
        
        :param source: Error source, must be file
        :type  source: str|unicode
        
        :param type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
        :type  type: str|unicode
        
        :param file_hash: Base64-encoded file hash
        :type  file_hash: str|unicode
        
        :param message: Error message
        :type  message: str|unicode
        
    
        Optional keyword parameters:
        """
        super(PassportElementErrorFile, self).__init__()
        assert_type_or_raise(source, unicode_type, parameter_name="source")
        self.source = source
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(file_hash, unicode_type, parameter_name="file_hash")
        self.file_hash = file_hash
        
        assert_type_or_raise(message, unicode_type, parameter_name="message")
        self.message = message
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportElementErrorFile to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportElementErrorFile, self).to_array()
        array['source'] = u(self.source)  # py2: type unicode, py3: type str
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['file_hash'] = u(self.file_hash)  # py2: type unicode, py3: type str
        array['message'] = u(self.message)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportElementErrorFile from a given dictionary.

        :return: new PassportElementErrorFile instance.
        :rtype: PassportElementErrorFile
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['source'] = u(array.get('source'))
        data['type'] = u(array.get('type'))
        data['file_hash'] = u(array.get('file_hash'))
        data['message'] = u(array.get('message'))
        
        instance = PassportElementErrorFile(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportelementerrorfile_instance)`
        """
        return "PassportElementErrorFile(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportelementerrorfile_instance)`
        """
        if self._raw:
            return "PassportElementErrorFile.from_array({self._raw})".format(self=self)
        # end if
        return "PassportElementErrorFile(source={self.source!r}, type={self.type!r}, file_hash={self.file_hash!r}, message={self.message!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportelementerrorfile_instance`
        """
        return key in ["source", "type", "file_hash", "message"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class PassportElementErrorFile



class PassportElementErrorFiles(PassportElementError):
    """
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    https://core.telegram.org/bots/api#passportelementerrorfiles
    

    Parameters:
    
    :param source: Error source, must be files
    :type  source: str|unicode
    
    :param type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
    :type  type: str|unicode
    
    :param file_hashes: List of base64-encoded file hashes
    :type  file_hashes: list of str|unicode
    
    :param message: Error message
    :type  message: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, source, type, file_hashes, message):
        """
        Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
    
        https://core.telegram.org/bots/api#passportelementerrorfiles
        
    
        Parameters:
        
        :param source: Error source, must be files
        :type  source: str|unicode
        
        :param type: The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”
        :type  type: str|unicode
        
        :param file_hashes: List of base64-encoded file hashes
        :type  file_hashes: list of str|unicode
        
        :param message: Error message
        :type  message: str|unicode
        
    
        Optional keyword parameters:
        """
        super(PassportElementErrorFiles, self).__init__()
        assert_type_or_raise(source, unicode_type, parameter_name="source")
        self.source = source
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(file_hashes, list, parameter_name="file_hashes")
        self.file_hashes = file_hashes
        
        assert_type_or_raise(message, unicode_type, parameter_name="message")
        self.message = message
    # end def __init__

    def to_array(self):
        """
        Serializes this PassportElementErrorFiles to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PassportElementErrorFiles, self).to_array()
        array['source'] = u(self.source)  # py2: type unicode, py3: type str
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['file_hashes'] = self._as_array(self.file_hashes)  # type list of str
        array['message'] = u(self.message)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PassportElementErrorFiles from a given dictionary.

        :return: new PassportElementErrorFiles instance.
        :rtype: PassportElementErrorFiles
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['source'] = u(array.get('source'))
        data['type'] = u(array.get('type'))
        data['file_hashes'] = PassportElementErrorFiles._builtin_from_array_list(required_type=unicode_type, value=array.get('file_hashes'), list_level=1)
        data['message'] = u(array.get('message'))
        
        instance = PassportElementErrorFiles(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(passportelementerrorfiles_instance)`
        """
        return "PassportElementErrorFiles(source={self.source!r}, type={self.type!r}, file_hashes={self.file_hashes!r}, message={self.message!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(passportelementerrorfiles_instance)`
        """
        if self._raw:
            return "PassportElementErrorFiles.from_array({self._raw})".format(self=self)
        # end if
        return "PassportElementErrorFiles(source={self.source!r}, type={self.type!r}, file_hashes={self.file_hashes!r}, message={self.message!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in passportelementerrorfiles_instance`
        """
        return key in ["source", "type", "file_hashes", "message"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class PassportElementErrorFiles

