from src.common.aml_ini_parser import AmlParserIniBase, AmlParserIniManager
import src.audio.aml_debug_audio

def instance(parser):
    return AmlParserIniAudio(parser)

class AmlParserIniAudio(AmlParserIniBase):
    AML_PARSER_AUDIO_CAPTRUE_MODE                   = "captrue_mode"
    AML_PARSER_AUDIO_DEBUG_INFO                     = "debug_info"
    AML_PARSER_AUDIO_DUMP_DATA                      = "dump_data"
    AML_PARSER_AUDIO_LOGCAT                         = "logcat"
    AML_PARSER_AUDIO_CAPTURE_TIME                   = "captrue_time"
    AML_PARSER_AUDIO_PRINT_DEBUG                    = "print_debug"
    AML_PARSER_AUDIO_CREATE_ZIP                     = "create_zip"
    def __init__(self, parser):
        super(AmlParserIniAudio, self).__init__(parser)
        self.m_section = AmlParserIniManager.AML_PARSER_SECTION_AUDIO

    def init_default_value(self):
        self.__dictionary_default_value = {
            AmlParserIniAudio.AML_PARSER_AUDIO_CAPTRUE_MODE      : str(src.audio.aml_debug_audio.DEFAULT_CAPTURE_MODE),
            AmlParserIniAudio.AML_PARSER_AUDIO_DEBUG_INFO        : 'True',
            AmlParserIniAudio.AML_PARSER_AUDIO_DUMP_DATA         : 'True',
            AmlParserIniAudio.AML_PARSER_AUDIO_LOGCAT            : 'True',
            AmlParserIniAudio.AML_PARSER_AUDIO_CAPTURE_TIME      : str(src.audio.aml_debug_audio.DEFAULT_AUTO_MODE_DUMP_TIME_S),
            AmlParserIniAudio.AML_PARSER_AUDIO_PRINT_DEBUG       : 'Flase',
            AmlParserIniAudio.AML_PARSER_AUDIO_CREATE_ZIP        : 'Flase',
        }
        return self.__dictionary_default_value
    
    def getValueByKey(self, key):
        if key == AmlParserIniAudio.AML_PARSER_AUDIO_CAPTRUE_MODE or   \
            key == AmlParserIniAudio.AML_PARSER_AUDIO_CAPTURE_TIME :
            return self.getIntValueByKey(key)
        elif key == AmlParserIniAudio.AML_PARSER_AUDIO_DEBUG_INFO or        \
            key == AmlParserIniAudio.AML_PARSER_AUDIO_DUMP_DATA or          \
            key == AmlParserIniAudio.AML_PARSER_AUDIO_LOGCAT or             \
            key == AmlParserIniAudio.AML_PARSER_AUDIO_PRINT_DEBUG or        \
            key == AmlParserIniAudio.AML_PARSER_AUDIO_CREATE_ZIP :
            return self.getBoolValueByKey(key)
        else :
            print('[E] AmlParserIniAudio::getValueByKey key:' + key + ', not support key.')
            return -1

    def setValueByKey(self, key, value):
        self.setStrValueByKey(key, str(value))