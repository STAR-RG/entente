import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

from subprocess import call


# @pytest.mark.skip(reason="temporarilly disabling")
def test_repos():
    path_name = os.path.join(constants.seeds_dir, 'repos')
    projects = [
        os.path.join(path_name, project_name)
        for project_name in os.listdir(path_name)
    ]
    for project_path in projects:
        multicall.multicall_directories(
            project_path, fuzzer='radamsa', validator=validate
        )

# def test_repos_100_javascript_projects():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '100-javascript-projects')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_12_javascript_quirks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '12-javascript-quirks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_123_Essential_JavaScript_Interview_Questions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '123-Essential-JavaScript-Interview-Questions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_30_seconds_of_code():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '30-seconds-of-code')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_30DaysOfJavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '30DaysOfJavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_30daysJavascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '30daysJavascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_33_js_concepts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '33-js-concepts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_4bottle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '4bottle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_500lines():
#     path_name = os.path.join(constants.seeds_dir, 'repos', '500lines')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ADE():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ADE')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AMD_feature():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AMD-feature')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_APE_JSF():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'APE_JSF')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_API():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'API')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_APIs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'APIs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Absolution():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Absolution')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AdNauseamV1():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AdNauseamV1')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AdminLTE():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AdminLTE')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AgileDwarf():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AgileDwarf')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Amanda():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Amanda')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Amplitude_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Amplitude-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AndEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AndEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AngularAdmin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AngularAdmin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AngularJS_Animation_Article():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AngularJS-Animation-Article')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AngularJS_SEO_Article():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AngularJS-SEO-Article')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AngularJs_UI():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AngularJs-UI')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AngularOverlay():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AngularOverlay')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AngularSlideables():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AngularSlideables')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AnimatedFrameSlideshow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AnimatedFrameSlideshow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AppScroll_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AppScroll.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Apprise():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Apprise')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Apricot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Apricot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AtomicGameEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AtomicGameEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AudioKeys():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AudioKeys')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AuthenticationAngularJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AuthenticationAngularJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Awesome_Design_Tools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Awesome-Design-Tools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Awesome_JavaScript_Interviews():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Awesome-JavaScript-Interviews')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_AwesomeChartJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'AwesomeChartJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Babylon_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Babylon.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Backbone_Mediator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Backbone-Mediator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Backbone_Rel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Backbone.Rel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Balloon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Balloon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_BananaBread():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'BananaBread')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Behaviour_Assertion_Sheets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Behaviour-Assertion-Sheets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Better_Autocomplete():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Better-Autocomplete')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_BitGoJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'BitGoJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Bitcoin_JavaScript_Miner():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Bitcoin-JavaScript-Miner')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_BlogEngine_NET():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'BlogEngine.NET')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Boostnote():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Boostnote')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Bootstrap_Scroll_Modal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Bootstrap-Scroll-Modal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Boxer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Boxer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Brackets_InteractiveLinter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Brackets-InteractiveLinter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Brewr_Site():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Brewr-Site')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Broadway():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Broadway')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_BrowserQuest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'BrowserQuest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_CPS_OCR_Engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'CPS-OCR-Engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Chakra_Samples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Chakra-Samples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ChakraCore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ChakraCore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ChariTi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ChariTi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Chart_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Chart.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Chatty():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Chatty')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Chroma_Hash():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Chroma-Hash')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ChromeAppHeroes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ChromeAppHeroes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Cinderblock():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Cinderblock')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Citrus_Engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Citrus-Engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_CodeMirror():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'CodeMirror')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_CoderDeck():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'CoderDeck')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Codestrong():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Codestrong')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Cookies():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Cookies')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Cordova():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Cordova')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Crafty():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Crafty')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Croppie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Croppie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Crunch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Crunch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_CtCI_6th_Edition_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'CtCI-6th-Edition-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_CtCI_6th_Edition_JavaScript_ES2015():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'CtCI-6th-Edition-JavaScript-ES2015')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_CuraEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'CuraEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_D3xter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'D3xter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_DEPRECATED_node_wit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'DEPRECATED-node-wit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_DEPRECATED_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'DEPRECATED.javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Daily_Interview_Question():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Daily-Interview-Question')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Datatables_Bootstrap3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Datatables-Bootstrap3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Datejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Datejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Demo_for_National_Geographic_Forest_Giant():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Demo-for-National-Geographic-Forest-Giant')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Design_Patterns_in_Javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Design-Patterns-in-Javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Device_Art_Generator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Device-Art-Generator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_DoFler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'DoFler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_DoloresLabsTechTalk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'DoloresLabsTechTalk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Donatello():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Donatello')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Dory():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Dory')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_DragonBonesJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'DragonBonesJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Dualx():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Dualx')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_DynamicGrid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'DynamicGrid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ES5_DOM_SHIM():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ES5-DOM-SHIM')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_EasyWebsocket():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'EasyWebsocket')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Editr_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Editr.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Effect_Games():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Effect-Games')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Efficient_Mobile_Web_FE_Development():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Efficient-Mobile-Web-FE-Development')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ElastiStack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ElastiStack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Eloquent_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Eloquent-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_EmberSockets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'EmberSockets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Emmet_codaplugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Emmet.codaplugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Espruino():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Espruino')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_EtherSheet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'EtherSheet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_EventEmitter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'EventEmitter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_FLAnimatedImage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'FLAnimatedImage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Fable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Fable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Face_Detection_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Face-Detection-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Face_Recognition_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Face-Recognition-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_FaustCplus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'FaustCplus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Fe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Fe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_FlappyBird_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'FlappyBird-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Flickable_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Flickable.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Flotr2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Flotr2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Font_Awesome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Font-Awesome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Force_com_JavaScript_REST_Toolkit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Force.com-JavaScript-REST-Toolkit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)



#  def test_repos_FramerTeachExamples():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'FramerTeachExamples')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_Front_End_Checklist():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Front-End-Checklist')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Full_Stack_JavaScript_Engineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Full-Stack-JavaScript-Engineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Functional_Light_JS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Functional-Light-JS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Fuse():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Fuse')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_G6():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'G6')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GLOW():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GLOW')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GSAP():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GSAP')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GameBoy_Online():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GameBoy-Online')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Garbochess_JS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Garbochess-JS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GeoMap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GeoMap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Ghost():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Ghost')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GitHubPopular_SJ():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GitHubPopular-SJ')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Glisse_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Glisse.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GloveBox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GloveBox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Google_Earth_Engine_JavaScript_Examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Google-Earth-Engine-JavaScript-Examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_GraphEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'GraphEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Grid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Grid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Guiders_JS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Guiders-JS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_HTML5_Asteroids():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'HTML5-Asteroids')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Hardy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Hardy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Hasher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Hasher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Hazel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Hazel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Head_First_JavaScript_Programming():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Head-First-JavaScript-Programming')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_HoneyProxy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'HoneyProxy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Honeypot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Honeypot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Hyperglot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Hyperglot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Hyperlapse_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Hyperlapse.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Illustrator_Layer_Exporter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Illustrator-Layer-Exporter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ImageResolver():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ImageResolver')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ImmersiveEngineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ImmersiveEngineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Interpose():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Interpose')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Isomorphism_react_todomvc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Isomorphism-react-todomvc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JQuery_Combinators():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JQuery-Combinators')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JQuery_Mobile_Slide_Menu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JQuery-Mobile-Slide-Menu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JS_Interpreter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JS-Interpreter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JS_humanize():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JS-humanize')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSARToolKit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSARToolKit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSIL():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSIL')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSLint():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSLint')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSMin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSMin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSON_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSON-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSONloops():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSONloops')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSPatch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSPatch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSVerbalExpressions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSVerbalExpressions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JSbooks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JSbooks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JZoopraxiscope():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JZoopraxiscope')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_21_Days_Challenge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-21-Days-Challenge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Algorithms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Algorithms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Applications():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Applications')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Canvas_to_Blob():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Canvas-to-Blob')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Completions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Completions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_DOM_Tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-DOM-Tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Data_Structure():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Data-Structure')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Data_Structures():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Data-Structures')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Demos():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Demos')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Design_Patterns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Design-Patterns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Equality_Table():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Equality-Table')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Fundamentals():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Fundamentals')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Garden():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Garden')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_I():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-I')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_ID3_Reader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-ID3-Reader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_II():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-II')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_III():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-III')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_IV():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-IV')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Koans():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Koans')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Lessons():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Lessons')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Load_Image():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Load-Image')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_MD5():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-MD5')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_OOP():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-OOP')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Particle_System():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Particle-System')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Playing_Cards():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Playing-Cards')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Quiz():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Quiz')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Scope_Context_Coloring():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Scope-Context-Coloring')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Snake():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Snake')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Templates():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Templates')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_Utilities():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-Utilities')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_autoComplete():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-autoComplete')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_cheat_sheet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-cheat-sheet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_for_Everyone():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-for-Everyone')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript_snippets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript-snippets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript1():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript1')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript30():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript30')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScript30_liyuechun():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScript30-liyuechun')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptAlgorithms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptAlgorithms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptBridge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptBridge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptCore_Demo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptCore-Demo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptCore_iOS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptCore-iOS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptEngineSwitcher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptEngineSwitcher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptEnhancements():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptEnhancements')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptIssuesStudy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptIssuesStudy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptServices():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptServices')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptStudy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptStudy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptTraining():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptTraining')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptTutorials():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptTutorials')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScriptViewEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScriptViewEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavaScripter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavaScripter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_Backdoor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript-Backdoor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_Equal_Height_Responsive_Rows():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript-Equal-Height-Responsive-Rows')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_Keylogger():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript-Keylogger')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_Undo_Manager():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript-Undo-Manager')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_Voronoi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript-Voronoi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_the_Good_Parts_notes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript-the-Good-Parts-notes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Javascript_Net():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Javascript.Net')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JavascriptSubtitlesOctopus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JavascriptSubtitlesOctopus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Jcrop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Jcrop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Jquery_Price_Format():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Jquery-Price-Format')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JsBridge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JsBridge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JsFormat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JsFormat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JsSIP():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JsSIP')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_JsSpeechRecognizer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'JsSpeechRecognizer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Jsome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Jsome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Jsource():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Jsource')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Juicer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Juicer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Kalendae():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Kalendae')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Kalm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Kalm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Kizzy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Kizzy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Kojak():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Kojak')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LABjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LABjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LJSON():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LJSON')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LLJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LLJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Leaflet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Leaflet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LeapJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LeapJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Learn_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Learn-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Leo_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Leo-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LiteAccordion():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LiteAccordion')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LokiJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LokiJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Lottery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Lottery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_LumixEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'LumixEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_MGTwitterEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'MGTwitterEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Maple_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Maple.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_MarkdownPresenter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'MarkdownPresenter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Marketing_for_Engineers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Marketing-for-Engineers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_MegEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'MegEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Memeye():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Memeye')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_MeteorRider():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'MeteorRider')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Mock():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Mock')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Modern_JavaScript_Curriculum():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Modern-JavaScript-Curriculum')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Modernizr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Modernizr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Monorail_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Monorail.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Motrix():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Motrix')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_NG6_todomvc_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'NG6-todomvc-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_NativeBase():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'NativeBase')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_New_Media_Image_Uploader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'New-Media-Image-Uploader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_NiL_JS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'NiL.JS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Numeral_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Numeral-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_OS_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'OS.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Object_observe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Object.observe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Octosplit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Octosplit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_OfflineMbTiles():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'OfflineMbTiles')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Oimo_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Oimo.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Openframe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Openframe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_OverReact():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'OverReact')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PHP_Vars_To_Js_Transformer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PHP-Vars-To-Js-Transformer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PNGDrive():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PNGDrive')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Parse_SDK_JS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Parse-SDK-JS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PexJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PexJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PhantomXHR():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PhantomXHR')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PhoneNumber_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PhoneNumber.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Phonegap_SQLitePlugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Phonegap-SQLitePlugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PhotoSwipe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PhotoSwipe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PhysicsJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PhysicsJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PixelJihad():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PixelJihad')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PowerBI_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PowerBI-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PptxGenJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PptxGenJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Presenteer_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Presenteer.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PreventSpider():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PreventSpider')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Programing_In_Javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Programing-In-Javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Proton():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Proton')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PubSubJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PubSubJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Pumpkin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Pumpkin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Pure_JavaScript_HTML5_Parser():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Pure-JavaScript-HTML5-Parser')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_PureSlider():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'PureSlider')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Push_It():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Push-It')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_QuickJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'QuickJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_QuoJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'QuoJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_RCSS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'RCSS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_RN_NavigationExperimental_Redux_Example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'RN-NavigationExperimental-Redux-Example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ROMManagerManifest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ROMManagerManifest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Radio():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Radio')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_RazorEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'RazorEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Reasons_Craft():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Reasons-Craft')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ReplayLastGoal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ReplayLastGoal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_RequireJS_Backbone_Starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'RequireJS-Backbone-Starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Revenant():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Revenant')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Rocket_Chat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Rocket.Chat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Rucksack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Rucksack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_RxJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'RxJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SJSJ():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SJSJ')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ScriptCommunicator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ScriptCommunicator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ScriptCraft():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ScriptCraft')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ScrollMagic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ScrollMagic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Scrolld_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Scrolld.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Scroller():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Scroller')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SeetaFaceEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SeetaFaceEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Selecter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Selecter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Semantic_UI():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Semantic-UI')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SendBird_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SendBird-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Serious_Engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Serious-Engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SilkJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SilkJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Sketch_Layer_Tools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Sketch-Layer-Tools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SketchGit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SketchGit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SketchSquares():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SketchSquares')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SketchToSwift():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SketchToSwift')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SlickGrid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SlickGrid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Snake_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Snake-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Snap_svg():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Snap.svg')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SocialFeed_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SocialFeed.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Sortable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Sortable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SpaceEngineers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SpaceEngineers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Sparky_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Sparky.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SpeechToText_WebSockets_Javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SpeechToText-WebSockets-Javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Sprint_Challenge__JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Sprint-Challenge--JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Sprint_Challenge_Applied_Javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Sprint-Challenge-Applied-Javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Starling_Framework():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Starling-Framework')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_StatusPage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'StatusPage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Stockfish():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Stockfish')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Streamus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Streamus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Strelki_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Strelki.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SublimeRubyMotionBuilder():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SublimeRubyMotionBuilder')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_SublimeTextSetupWiki():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'SublimeTextSetupWiki')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Switcheroo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Switcheroo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Syte2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Syte2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TOMODOkorz():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TOMODOkorz')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TableTools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TableTools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tangle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tangle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tangram_base():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tangram-base')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tangram_component():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tangram-component')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tangram2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tangram2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tasks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tasks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TemplateBinding():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TemplateBinding')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_The_complete_guide_to_modern_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'The-complete-guide-to-modern-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TheAmazingAudioEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TheAmazingAudioEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ThreeNodes_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ThreeNodes.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Throttle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Throttle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TiIconicFont():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TiIconicFont')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TimelineJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TimelineJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Titanium_Tools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Titanium-Tools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Todo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Todo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TopLevel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TopLevel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TouchyBP():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TouchyBP')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tracker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tracker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_TransformJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'TransformJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Tuiter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Tuiter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_TypeScript():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'TypeScript')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_UIWebView_TS_JavaScriptContext():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'UIWebView-TS_JavaScriptContext')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_URI_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'URI.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_UTiL():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'UTiL')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_UglifyJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'UglifyJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_UglifyJS2():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'UglifyJS2')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_UnrealEnginePython():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'UnrealEnginePython')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_V2EX_Vue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'V2EX-Vue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_V8():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'V8')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Validator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Validator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Vanilla_JavaScript_Calculator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Vanilla-JavaScript-Calculator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ViewerJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ViewerJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_VvvebJs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'VvvebJs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WKWebViewJavascriptBridge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WKWebViewJavascriptBridge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Walkable_App():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Walkable-App')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WalletGenerator_net():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WalletGenerator.net')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WasAPlayer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WasAPlayer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WeApp_Workflow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WeApp-Workflow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WebCola():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WebCola')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WebODF():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WebODF')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WebViewJavascriptBridge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WebViewJavascriptBridge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Webiny():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Webiny')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Webplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Webplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WickedEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WickedEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_WickedGrid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'WickedGrid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_You_Dont_Know_JS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'You-Dont-Know-JS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_You_Dont_Need_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'You-Dont-Need-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_You_Dont_Need_jQuery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'You-Dont-Need-jQuery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_YouCompleteMe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'YouCompleteMe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_Zoombox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'Zoombox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_a_triangle_everyday():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'a-triangle-everyday')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_abba():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'abba')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_acc_wizard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'acc-wizard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ace():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ace')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_acorn():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'acorn')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_acs_engine():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'acs-engine')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_activejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'activejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_adblock_to_bitcoin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'adblock-to-bitcoin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_adminjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'adminjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_advanced_jquery_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'advanced-jquery-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_aima_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'aima-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_airbrake_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'airbrake-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_airtable_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'airtable.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_aks_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'aks-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_alertify_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'alertify.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_algoliasearch_client_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'algoliasearch-client-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_algorithm_visualizer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'algorithm-visualizer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_allora():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'allora')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_alphabeta():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'alphabeta')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_amazeui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'amazeui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_amazon_cognito_identity_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'amazon-cognito-identity-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_amcharts3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'amcharts3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ammo_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ammo.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_amphtml():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'amphtml')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_amplify_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'amplify-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_amqp_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'amqp-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_anchor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'anchor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_aside():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-aside')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_block_ui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-block-ui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_bootstrap_switch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-bootstrap-switch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_chartjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-chartjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_clipboard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-clipboard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_collection():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-collection')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_d3_demo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-d3-demo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_deferred_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-deferred-bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_directive_g_signin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-directive.g-signin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_drop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-drop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_electron():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-electron')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_ellipsis():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-ellipsis')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_fabric():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-fabric')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_formly():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-formly')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_google_maps():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-google-maps')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_guide_zh():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-guide-zh')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_gulp_browserify_livereload_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-gulp-browserify-livereload-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_hateoas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-hateoas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_history():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-history')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_indexedDB():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-indexedDB')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_load():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-load')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_md5():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-md5')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_mobile_ui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-mobile-ui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_multiselect():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-multiselect')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_notifications():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-notifications')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_oauth():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-oauth')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_once():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-once')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_parse():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-parse')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_patternfly():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-patternfly')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_promise_buttons():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-promise-buttons')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_react_native_seed():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-react-native-seed')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_redactor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-redactor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_responsive():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-responsive')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_sails_bind():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-sails-bind')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_socket_io_im():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-socket-io-im')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_timeago():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-timeago')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_toArrayFilter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-toArrayFilter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_typeahead():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-typeahead')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_ui_tour():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-ui-tour')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_validation_match():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-validation-match')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_validator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-validator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_video_bg():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-video-bg')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_virtual_scroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-virtual-scroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_webstorage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular-webstorage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular1_systemjs_seed():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular1-systemjs-seed')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular1_webpack_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular1-webpack-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular2_now():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular2-now')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angular2_the_new_horizon_sample():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angular2-the-new-horizon-sample')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularJS_CafeTownsend():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularJS-CafeTownsend')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_FlightDashboard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-FlightDashboard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_geolocation():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-geolocation')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_imageupload_directive():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-imageupload-directive')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_modal_service():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-modal-service')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_performance_tips():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-performance-tips')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_periscope():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-periscope')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_requirejs_lazy_controllers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-requirejs-lazy-controllers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_seed_repo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-seed-repo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_server():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-server')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs_utilities():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs-utilities')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_angularjs1():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'angularjs1')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_anime():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'anime')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ansi_canvas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ansi-canvas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ant_design():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ant-design')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_apejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'apejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_apexcharts_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'apexcharts.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_app_id_sanity():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'app-id-sanity')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_appengine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'appengine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_appframework():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'appframework')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_aprendendo_padroes_de_projeto_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'aprendendo-padroes-de-projeto-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_archived_morkdown():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'archived-morkdown')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_art_template():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'art-template')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_asch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'asch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_assemblies():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'assemblies')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_asteroid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'asteroid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_async():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'async')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_async_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'async-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_async_javascript_cheatsheet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'async-javascript-cheatsheet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_async_javascript_workshop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'async-javascript-workshop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_atmosphere_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'atmosphere-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_atom():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'atom')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_atom_javascript_snippets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'atom-javascript-snippets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_atom_react_snippets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'atom-react-snippets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_atom_turbo_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'atom-turbo-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_atomus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'atomus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_aurora_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'aurora.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_auth0_javascript_samples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'auth0-javascript-samples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_authenticator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'authenticator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_autobahn_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'autobahn-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_automaton():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'automaton')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_autopolyfiller():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'autopolyfiller')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_autoprefixer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'autoprefixer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_autoprefixer_loader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'autoprefixer-loader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ava():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ava')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ava_spec():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ava-spec')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_avsc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'avsc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_chaos_engineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-chaos-engineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_data_engineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-data-engineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_javascript_cn():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-javascript-cn')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_javascript_learning():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-javascript-learning')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_mac():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-mac')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_react_native():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-react-native')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_reverse_engineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-reverse-engineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_selfhosted():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-selfhosted')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awesome_vscode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awesome-vscode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awponent():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awponent')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_aws_lambda_debugger():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'aws-lambda-debugger')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_aws2js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'aws2js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_awsdetailedbilling():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'awsdetailedbilling')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_axios():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'axios')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_babel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'babel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_babel_plugin_webpack_loaders():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'babel-plugin-webpack-loaders')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_babel_webpack_tree_shaking():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'babel-webpack-tree-shaking')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_express_spa():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone-express-spa')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_jquerymobile():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone-jquerymobile')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_mobile_search():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone-mobile-search')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_pouch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone-pouch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_analytics():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone.analytics')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_directives():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone.directives')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_geppetto():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone.geppetto')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_googlemaps():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone.googlemaps')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_memento():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone.memento')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbone_modal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbone.modal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backbonefire():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backbonefire')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_backtick():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'backtick')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bank():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bank')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bbGrid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bbGrid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bcoin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bcoin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_be_MEAN_resources():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'be-MEAN-resources')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_beamjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'beamjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_beatdetektor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'beatdetektor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_beginner_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'beginner-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bem_bl():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bem-bl')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bem_tools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bem-tools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_benjamin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'benjamin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_better_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'better.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_between():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'between')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_between_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'between.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bgiframe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bgiframe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bic_calendar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bic_calendar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_big_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'big.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bitaddress_org():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bitaddress.org')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bitcoinjs_lib():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bitcoinjs-lib')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bitcore_lib():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bitcore-lib')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_blessed_contrib():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'blessed-contrib')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bliss():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bliss')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_blockparty():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'blockparty')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_blog_swift():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'blog.swift')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bluebird():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bluebird')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bn_javascript_info():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bn.javascript.info')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bn_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bn.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_boa():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'boa')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_boilerplatejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'boilerplatejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_boilerstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'boilerstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bonescript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bonescript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_boom():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'boom')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_boombox_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'boombox.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_datepaginator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap-datepaginator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_file_input():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap-file-input')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_ios7():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap-ios7')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_tldr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap-tldr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_toggle_buttons():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap-toggle-buttons')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_xtra():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap-xtra')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bootstrap_isotope():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bootstrap_isotope')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_botui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'botui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bower():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bower')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_box2d():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'box2d')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_box2d_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'box2d-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bpipe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bpipe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bpmn_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bpmn-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_brackets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'brackets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_brain_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'brain.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_brfv4_javascript_examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'brfv4_javascript_examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_brisket():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'brisket')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_broadway():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'broadway')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_browser_pwn():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'browser_pwn')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_browserify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'browserify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_brozula():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'brozula')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bselect():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bselect')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bubbletree():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bubbletree')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bui_default():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bui-default')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_building_products_with_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'building-products-with-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bus_io():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bus.io')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_bwip_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'bwip-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_c3netmon_public():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'c3netmon-public')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cactbot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cactbot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_calendarHTML_Javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'calendarHTML-Javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_canibekikked():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'canibekikked')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cannon_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cannon.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_canvg():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'canvg')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_capt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'capt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_car_lease_demo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'car-lease-demo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_carbon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'carbon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_caribou():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'caribou')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_carto_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'carto.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cash():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cash')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_casual():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'casual')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cats():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cats')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ccss():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ccss')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ccxt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ccxt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cdir():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cdir')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cedar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cedar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chain_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chain.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chalk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chalk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chancejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chancejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_channel_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'channel.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chaosocket():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chaosocket')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chapters():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chapters')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_charlie_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'charlie.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chartkick():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chartkick')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chatter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chatter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cheat_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cheat-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cheatsheets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cheatsheets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_checkboxes_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'checkboxes.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_checkerboard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'checkerboard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_checkpoint_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'checkpoint-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cheerio():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cheerio')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chessboardjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chessboardjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chevrotain():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chevrotain')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chinese_poetry():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chinese-poetry')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chroma_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chroma.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chrome_nfc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chrome-nfc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chromecast_gb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chromecast-gb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_chrono():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'chrono')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_circleci_demo_javascript_express():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'circleci-demo-javascript-express')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_clarifai_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'clarifai-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_clarifyjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'clarifyjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_classnames():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'classnames')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_clean_code_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'clean-code-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_clean_code_javascript_tr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'clean-code-javascript-tr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_clean_code_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'clean-code-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cleverstack_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cleverstack-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_client_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'client-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_clipboard_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'clipboard.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cloak():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cloak')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_closure_compiler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'closure-compiler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_closure_library():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'closure-library')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cloudboost():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cloudboost')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cloudinary_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cloudinary_js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cms_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cms.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_co_express():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'co-express')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_co_mocha():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'co-mocha')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_co_request():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'co-request')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cocos2d_html5():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cocos2d-html5')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cocos2d_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cocos2d-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_codaslider():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'codaslider')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_code_editor_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'code-editor-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_code_splitting_react_webpack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'code-splitting-react-webpack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_codeblock_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'codeblock.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_codem_transcode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'codem-transcode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_codemirror_movie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'codemirror-movie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_codesurgeon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'codesurgeon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_coffeescript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'coffeescript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_coffin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'coffin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_coloor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'coloor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_color():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'color')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_color_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'color.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_colovely():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'colovely')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_combinatorics_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'combinatorics.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_command_and_conquer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'command-and-conquer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_commander_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'commander.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_commonmark_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'commonmark.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_compass_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'compass-bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_complete():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'complete')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_complete_javascript_course():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'complete-javascript-course')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_complexity_report():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'complexity-report')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_component_installer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'component-installer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_composition_examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'composition-examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_compressorjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'compressorjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_computer_science_in_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'computer-science-in-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_conductor_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'conductor.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_congo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'congo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_connect_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'connect-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_connect_mongodb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'connect-mongodb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_contracts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'contracts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_converse_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'converse.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_coquette():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'coquette')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cordova_plugin_console():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cordova-plugin-console')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cordova_plugin_wkwebview_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cordova-plugin-wkwebview-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_couchpubtato():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'couchpubtato')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_coverify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'coverify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_covert():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'covert')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_create_react_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'create-react-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_creditcard_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'creditcard_js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_creditly():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'creditly')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cropit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cropit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cropperjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cropperjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_crossbow_sites():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'crossbow-sites')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_crossroads_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'crossroads.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cruncher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cruncher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_crypto_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'crypto-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_crypto_pouch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'crypto-pouch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_csonv_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'csonv.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cspjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cspjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_css_modules_demos():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'css-modules-demos')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_css_modules_require_hook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'css-modules-require-hook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_css_regions_polyfill():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'css-regions-polyfill')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_css_reporter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'css-reporter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_css3_mediaqueries_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'css3-mediaqueries-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cssConsole():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cssConsole')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_csscritic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'csscritic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cssfilterlab():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cssfilterlab')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cst():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cst')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cubism():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cubism')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cucumber_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cucumber-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cult():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cult')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_currency_io():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'currency.io')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_curso_definitivo_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'curso-definitivo-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_curso_javascript_avanzado():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'curso-javascript-avanzado')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_curso_javascript_ninja():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'curso-javascript-ninja')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_curso_javascript_projeto_usuarios():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'curso-javascript-projeto-usuarios')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_curso_sistemas_web_com_spring_javascript_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'curso-sistemas-web-com-spring-javascript-bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cyclejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cyclejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_cypress():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'cypress')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3_cloud():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3-cloud')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3_dot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3-dot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3_react_squared():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3-react-squared')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3_starterkit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3-starterkit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3AngularIntegration():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3AngularIntegration')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_d3talk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'd3talk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dagre():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dagre')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_darkstripes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'darkstripes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dat_gui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dat.gui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_data_projector():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'data-projector')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_data_structures_and_algorithms_using_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'data_structures_and_algorithms_using_javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dataflow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dataflow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_datavore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'datavore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_date_fns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'date-fns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_daterangepicker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'daterangepicker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_datui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'datui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dayjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dayjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_db():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'db')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_deamdify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'deamdify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_debug_http():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'debug-http')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_decaffeinate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'decaffeinate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_decimal_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'decimal.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_decking():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'decking')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_def_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'def.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_delaunay_fast():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'delaunay-fast')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_delorean():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'delorean')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_demopack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'demopack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_demystifying_js_engines():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'demystifying-js-engines')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_den():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'den')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_deno():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'deno')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_denodeify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'denodeify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_deprecated_electrode_archetype_react_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'deprecated-electrode-archetype-react-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_desantapp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'desantapp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_descartes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'descartes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_destiny():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'destiny')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_devoops():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'devoops')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dffptch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dffptch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dialogflow_javascript_client():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dialogflow-javascript-client')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_director():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'director')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_directory_backbone_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'directory-backbone-bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_discord_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'discord.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dive_into_python3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dive-into-python3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dizzy_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dizzy.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_django_chosen():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'django-chosen')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_django_drf_react_quickstart():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'django-drf-react-quickstart')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_do():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'do')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_doT():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'doT')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_docblockr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'docblockr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_docker_node():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'docker-node')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_docker_parse_server_git_deploy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'docker-parse-server-git-deploy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_docker_private_registry():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'docker-private-registry')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dockunit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dockunit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_doclets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'doclets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_docs2epub():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'docs2epub')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_doctestjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'doctestjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_documentation():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'documentation')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_docusaurus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'docusaurus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dom_elements():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dom-elements')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dotjs_addon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dotjs-addon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dotty():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dotty')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_download():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'download')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_downworthy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'downworthy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dpicker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dpicker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_draft_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'draft-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_draggable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'draggable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_draggable_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'draggable.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dragula():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dragula')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_drive_dredit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'drive-dredit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_drive_zipextractor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'drive-zipextractor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_driver_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'driver.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_drools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'drools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dropbox_sdk_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dropbox-sdk-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dropchop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dropchop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dropfile():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dropfile')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dropmocks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dropmocks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dropzone():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dropzone')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dsa_js_data_structures_algorithms_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dsa.js-data-structures-algorithms-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_duktape():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'duktape')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_duktape_android():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'duktape-android')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dva():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dva')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dynamics_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dynamics.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dynamo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dynamo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_dynode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'dynode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_earthengine_api():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'earthengine-api')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_easyModal_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'easyModal.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ec2_fleet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ec2-fleet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_echojs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'echojs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_echowaves():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'echowaves')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_eclipse_zencoding():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'eclipse-zencoding')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ect():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ect')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_effective_javascript():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'effective-javascript')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_egg():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'egg')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_egghead_react_flux_example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'egghead-react-flux-example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ej2_javascript_ui_controls():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ej2-javascript-ui-controls')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_elastic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'elastic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_elasticsearch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'elasticsearch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_electrode_server():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'electrode-server')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_electron():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'electron')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_electron_accelerator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'electron-accelerator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_elixirscript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'elixirscript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_elliptic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'elliptic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_elm_hot_loader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'elm-hot-loader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_eloquente_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'eloquente-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_animate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-animate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_async_button():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-async-button')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_auth():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-auth')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_burger_menu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-burger-menu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_cli_i18n():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-cli-i18n')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_cli_pace():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-cli-pace')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_cli_pagination():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-cli-pagination')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_cpm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-cpm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_crud():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-crud')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_data_django_rest_adapter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-data-django-rest-adapter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_data_route():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-data-route')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_forms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-forms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_graphql_adapter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-graphql-adapter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_islands():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-islands')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_json_api():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-json-api')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_parse_adapter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-parse-adapter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_resource():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-resource')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_rest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-rest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_restless():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-restless')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_select_2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-select-2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_skeleton():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-skeleton')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_touch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember-touch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ember_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ember.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_en_javascript_info():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'en.javascript.info')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_encog_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'encog-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_engine_io():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'engine.io')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_engineer_manager():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'engineer-manager')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_engineercms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'engineercms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_engineering_blogs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'engineering-blogs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_engineering_management():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'engineering-management')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_enigma_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'enigma.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_enquire_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'enquire.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_enzyme():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'enzyme')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_epf():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'epf')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es_papp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es-papp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es_javascript_info():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es.javascript.info')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es5_shim():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es5-shim')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es6_babel_browserify_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es6-babel-browserify-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es6_design_patterns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es6-design-patterns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es6_project_starter_kit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es6-project-starter-kit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es6_react_mixins():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es6-react-mixins')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_es6tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'es6tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_esbuild():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'esbuild')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_escargot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'escargot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_esdoc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'esdoc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_esercizi_di_programmazione_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'esercizi-di-programmazione-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_esformatter_jsx():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'esformatter-jsx')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_eslint():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'eslint')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_eslint_config_defaults():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'eslint-config-defaults')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_eslint_formatter_pretty():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'eslint-formatter-pretty')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_esperanto():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'esperanto')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_espree():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'espree')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_essage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'essage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_essential_javascript_links():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'essential-javascript-links')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_essential_js_design_patterns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'essential-js-design-patterns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_evee_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'evee.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_evernote_sdk_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'evernote-sdk-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ews_javascript_api():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ews-javascript-api')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ex_navigator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ex-navigator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_example_backbone_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'example-backbone-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_example_node():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'example-node')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_excel_builder_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'excel-builder.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_excellentexport():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'excellentexport')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_execjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'execjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_exercises():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'exercises')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_exokit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'exokit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_exoskeleton():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'exoskeleton')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_express():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'express')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_express_angular():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'express-angular')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_express_di():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'express-di')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_express_happiness():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'express-happiness')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_express_partials():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'express-partials')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_express_train():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'express-train')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_exterminate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'exterminate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_eyeballs_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'eyeballs.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_f8app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'f8app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fabric_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fabric.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_facebook_circles():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'facebook-circles')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_facebook_js_sdk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'facebook-js-sdk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_faced():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'faced')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fairy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fairy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_faker_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'faker.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_falcor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'falcor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_falkor_archived():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'falkor-archived')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fancy_zoom():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fancy-zoom')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fann_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fann.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fantasy_land():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fantasy-land')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fastify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fastify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fbt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fbt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fe_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fe.javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_feather():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'feather')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_feature_engineering_book():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'feature-engineering-book')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_feelingrestful_theme():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'feelingrestful-theme')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fela():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fela')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_felt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'felt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fetch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fetch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fhir_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fhir.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fibjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fibjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fieldval_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fieldval-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_filepond():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'filepond')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fileupload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fileupload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_finitio():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'finitio')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_firebase_angular_starter_pack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'firebase-angular-starter-pack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fireloop_io():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fireloop.io')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_firequery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'firequery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fireunit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fireunit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fireworks_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fireworks.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fishbone_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fishbone.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fiveby():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fiveby')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fixto():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fixto')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flaskr_tdd():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flaskr-tdd')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flatpickr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flatpickr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flexibility():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flexibility')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flight():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flight')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flipcountdown():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flipcountdown')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flipload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flipload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flotsam():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flotsam')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flow_jsdoc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flow-jsdoc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flowable_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flowable-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flowy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flowy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_flux_router_component():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'flux-router-component')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fmt_obj():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fmt-obj')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fn_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fn.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_font_awesome_webpack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'font-awesome-webpack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_forest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'forest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_formacao_javascript_mestre_jedi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'formacao-javascript-mestre-jedi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_formaline():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'formaline')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_formhub():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'formhub')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_formio_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'formio.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_formspree():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'formspree')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fourk_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fourk.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_foxjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'foxjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_frame_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'frame.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_framer_sketch_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'framer-sketch-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_framer_templates():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'framer-templates')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_framework():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'framework')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_framework7():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'framework7')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_framework7_react_base():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'framework7-react-base')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_freeCodeCamp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'freeCodeCamp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_front_end_interview_handbook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'front-end-interview-handbook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_front_end_separate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'front-end-separate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_front_ui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'front-ui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_frozen():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'frozen')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_frpjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'frpjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fruitmachine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fruitmachine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fseditor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fseditor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fuckitjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fuckitjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fullPage_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fullPage.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fullproof():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fullproof')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fullstack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fullstack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fullstack_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fullstack-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fullstack_javascript_architecture():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fullstack-javascript-architecture')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_functional_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'functional-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_functional_javascript_workshop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'functional-javascript-workshop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_functional_programming_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'functional-programming-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_fuzzilli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'fuzzilli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_galleria():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'galleria')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gamblers_dice():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gamblers-dice')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gameQuery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gameQuery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ganache_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ganache-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ganon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ganon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gantt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gantt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gatsby():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gatsby')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gauge_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gauge.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_geierlein():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'geierlein')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_angular_go_martini():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-angular-go-martini')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_angulpify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-angulpify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_jhipster():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-jhipster')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_jhipster_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-jhipster-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_jquery_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-jquery-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_phaser():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-phaser')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_polymer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-polymer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_generator_redux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'generator-redux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_geo_googledocs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'geo-googledocs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_geohash_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'geohash-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_getdocs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'getdocs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_getting_started_with_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'getting-started-with-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gh_emoji():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gh-emoji')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ghcjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ghcjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ghost_town():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ghost-town')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gif_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gif.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gijgo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gijgo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gilded_rose_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gilded-rose-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_git_watcher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'git-watcher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_git_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'git.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gitbook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gitbook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gitflowanimated():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gitflowanimated')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_github_notetaker_egghead():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'github-notetaker-egghead')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_github_s3_deploy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'github-s3-deploy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gitlet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gitlet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gl_matrix():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gl-matrix')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gloria():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gloria')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gmail_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gmail.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gnode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gnode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_go_duktape():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'go-duktape')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_go_for_javascript_developers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'go-for-javascript-developers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_go_v8():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'go-v8')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_goangular():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'goangular')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_godot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'godot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_godot_docs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'godot-docs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_goodnight():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'goodnight')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_google_api_javascript_client():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'google-api-javascript-client')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_google_plus_extension_jsapi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'google-plus-extension-jsapi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_google_spreadsheet_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'google-spreadsheet-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_google_tts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'google-tts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gplus_quickstart_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gplus-quickstart-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gpu_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gpu.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_graphitejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'graphitejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_graphql_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'graphql-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_graphql_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'graphql-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gremlin_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gremlin-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_growl4rails():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'growl4rails')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_bake():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-bake')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_bower_requirejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-bower-requirejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_browserify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-browserify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_closure_compiler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-closure-compiler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_contrib_compress():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-contrib-compress')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_contrib_csslint():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-contrib-csslint')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_css():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-css')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_email_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-email-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_express_server():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-express-server')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_git():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-git')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_githooks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-githooks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_html_snapshot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-html-snapshot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_html2js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-html2js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_hub():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-hub')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_imagine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-imagine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_includes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-includes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_inline_css():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-inline-css')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_jekyll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-jekyll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_markdown():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-markdown')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_nodemon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-nodemon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_phantomas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-phantomas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_premailer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-premailer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_reload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-reload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_requirejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-requirejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_s3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-s3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_grunt_text_replace():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'grunt-text-replace')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gua_game_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gua.game.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_guitar_bro():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'guitar_bro')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp_awspublish():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp-awspublish')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp_filter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp-filter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp_ignore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp-ignore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp_jscs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp-jscs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp_ng_config():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp-ng-config')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulp_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulp-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulpfiction():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulpfiction')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gulpman():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gulpman')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_gury():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'gury')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_h5ive_DEPRECATED():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'h5ive-DEPRECATED')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hackathon_casperjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hackathon-casperjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hackathon_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hackathon-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hacker_scripts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hacker-scripts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hacking_with_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hacking-with-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hackynote():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hackynote')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_haloword():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'haloword')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hammer_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hammer.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_handlebars_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'handlebars.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_handsontable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'handsontable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hapi_universal_redux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hapi-universal-redux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_haskell_ide_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'haskell-ide-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_haunt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'haunt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_headtrackr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'headtrackr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_heapbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'heapbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_heartbeat_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'heartbeat.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_heatmap_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'heatmap.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hello_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hello-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_henryyan_github_com():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'henryyan.github.com')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hermes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hermes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hexo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hexo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_highcharts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'highcharts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_highlight():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'highlight')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_highlight_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'highlight.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hiring_engineers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hiring-engineers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hiring_without_whiteboards():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hiring-without-whiteboards')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_history():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'history')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_history_of_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'history-of-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hitagi_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hitagi.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hivemind():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hivemind')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hls_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hls.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hn_ng2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hn-ng2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hn_reader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hn-reader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_holla():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'holla')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_homebridge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'homebridge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hoodie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hoodie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hookbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hookbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_horizon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'horizon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hotdot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hotdot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hotspots():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hotspots')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_how_javascript_works():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'how-javascript-works')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_how_to_sane():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'how-to-sane')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_howler_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'howler.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hpm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hpm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_html_minifier():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'html-minifier')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_html2canvas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'html2canvas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_html2jade_website():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'html2jade-website')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_html5_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'html5-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_htmljs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'htmljs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_http_client():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'http-client')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hubot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hubot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hummingbird():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hummingbird')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_huntsman():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'huntsman')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_husky():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'husky')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hyper_pokemon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hyper-pokemon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hyperglue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hyperglue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hyperscript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hyperscript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_hypher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'hypher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iClient_JavaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iClient-JavaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iCreator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iCreator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iD():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iD')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iMessageWebClient():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iMessageWebClient')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iOS_HTML5_Tethering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iOS-HTML5-Tethering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iOSAppReverseEngineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iOSAppReverseEngineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ice():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ice')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_icons():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'icons')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iconv_lite():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iconv-lite')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_idiomatic_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'idiomatic.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ie8():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ie8')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iioEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iioEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_imaskjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'imaskjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_imgr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'imgr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_imgsible():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'imgsible')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_immer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'immer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_immstruct():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'immstruct')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_immutable_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'immutable-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_impresionante_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'impresionante-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_impress_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'impress.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_incubator_echarts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'incubator-echarts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_inferno():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'inferno')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_infiniScroll_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'infiniScroll.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_infiniwall():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'infiniwall')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_inline_manifest_webpack_plugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'inline-manifest-webpack-plugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_inscribe_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'inscribe.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_instachrome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'instachrome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_instafeed_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'instafeed.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_instagram_javascript_sdk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'instagram-javascript-sdk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_intermediate_javascript_assessment():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'intermediate-javascript-assessment')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_interview_questions_in_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'interview-questions-in-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_intl_tel_input():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'intl-tel-input')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_intro_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'intro-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_inu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'inu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ioBroker_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ioBroker.javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ionic_demo_resort_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ionic-demo-resort-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ionic_modal_select():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ionic-modal-select')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ionic_ocr_example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ionic-ocr-example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iota_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iota.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iptv():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iptv')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ipython_vimception():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ipython-vimception')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_irecord():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'irecord')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iroha_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iroha-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iron_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iron-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_is_loading():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'is-loading')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_is_up_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'is-up-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_iscroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'iscroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_isomorphic_lab():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'isomorphic-lab')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_isomorphic_redux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'isomorphic-redux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_isotope_perfectmasonry():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'isotope-perfectmasonry')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_isparta_loader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'isparta-loader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jCryption():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jCryption')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQote2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQote2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Chrono():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Chrono')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Custom_File_Input():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Custom-File-Input')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Mobile_Boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Mobile-Boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Parse():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Parse')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Shadow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Shadow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Simple_Timer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Simple-Timer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Smart_Auto_Complete():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Smart-Auto-Complete')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Stickem():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Stickem')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Timepicker_Addon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Timepicker-Addon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Validation_Engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Validation-Engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_Verbose_Calendar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-Verbose-Calendar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_basic_arithmetic_plugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery-basic-arithmetic-plugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_loadScroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery.loadScroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jQuery_stayInWebApp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jQuery.stayInWebApp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jWorkflow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jWorkflow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jaadi_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jaadi.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jarallax():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jarallax')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jarves():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jarves')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jasmine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jasmine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jasmine_fixture():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jasmine-fixture')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jasmine_sinon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jasmine-sinon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jasmine_async():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jasmine.async')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javaScript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javaScript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javaee_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javaee-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_1_afternoon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-1-afternoon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_101():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-101')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_2_afternoon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-2-afternoon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_2_afternoon_2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-2-afternoon-2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_2_afternoon_3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-2-afternoon-3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_3_afternoon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-3-afternoon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_5_lodash():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-5-lodash')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_action():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-action')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_airbnb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-airbnb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_algorithms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-algorithms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_allonge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-allonge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_arithmetic_lab_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-arithmetic-lab-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_arrays_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-arrays-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_arrays_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-arrays-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_arrays_lab_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-arrays-lab-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_astar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-astar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_barcode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-barcode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_basic_assessment():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-basic-assessment')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_basics():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-basics')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_biginteger():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-biginteger')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_bignum():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-bignum')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_bootcamp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-bootcamp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_challenges():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-challenges')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_challenges_book():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-challenges-book')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_conferences():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-conferences')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_crypto_library():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-crypto-library')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_datastructures_algorithms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-datastructures-algorithms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_debug():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-debug')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_decorators():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-decorators')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_design_patterns_for_humans():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-design-patterns-for-humans')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_detect_element_resize():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-detect-element-resize')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_development_environment():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-development-environment')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_dom():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-dom')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_drones():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-drones')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_ebooks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-ebooks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_empire():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-empire')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_enlightenment():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-enlightenment')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_error_logging():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-error-logging')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_errors_notifier():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-errors-notifier')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_exercises():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-exercises')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_fetch_lab():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-fetch-lab')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_fix_the_scope_lab_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-fix-the-scope-lab-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_fix_the_scope_lab_js_apply_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-fix-the-scope-lab-js-apply-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_fix_the_scope_lab_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-fix-the-scope-lab-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_for_cats():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-for-cats')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_foundations():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-foundations')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_gauntlet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-gauntlet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_guessing_game():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-guessing-game')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_hide_and_seek_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-hide-and-seek-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_in_14_minutes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-in-14-minutes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_in_one_pic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-in-one-pic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_inspirate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-inspirate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_interview():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-interview')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_interview_questions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-interview-questions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_intro_to_functions_lab_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-intro-to-functions-lab-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_intro_to_functions_lab_js_apply_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-intro-to-functions-lab-js-apply-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_intro_to_looping_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-intro-to-looping-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_intro_to_looping_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-intro-to-looping-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_journey():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-journey')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_jpeg_encoder():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-jpeg-encoder')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_jquery_ruble():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-jquery.ruble')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_kit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-kit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_koans():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-koans')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_last_fm_api():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-last.fm-api')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_lessons():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-lessons')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_libraries_syntax_vim():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-libraries-syntax.vim')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_linkify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-linkify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_logging_lab_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-logging-lab-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_logging_lab_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-logging-lab-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_malware_collection():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-malware-collection')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_mobile_desktop_geolocation():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-mobile-desktop-geolocation')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_natural_sort():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-natural-sort')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_notes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-notes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_javascript_obfuscator():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-obfuscator')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_javascript_obfuscator_ui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-obfuscator-ui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_objects_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-objects-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_objects_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-objects-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_objects_lab_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-objects-lab-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_opentimestamps():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-opentimestamps')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_path():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-path')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_patterns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-patterns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_piano():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-piano')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_pong():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-pong')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_profesional():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-profesional')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_professional():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-professional')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_questions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-questions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_quiz():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-quiz')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_racer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-racer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_risingstars():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-risingstars')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_robotics():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-robotics')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_rock_dodger_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-rock-dodger-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_rsa():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-rsa')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_samples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-samples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_sandbox_console():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-sandbox-console')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_sdk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-sdk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_sdk_design():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-sdk-design')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_simon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-simon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_snakes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-snakes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_starter_course():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-starter-course')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_state_machine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-state-machine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_strings_lab_js_apply_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-strings-lab-js-apply-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_strings_lab_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-strings-lab-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_style_guide():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-style-guide')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_test_reporter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-test-reporter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_testing_best_practices():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-testing-best-practices')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tests():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tests')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tetris():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tetris')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_time_ago():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-time-ago')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tiny_platformer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tiny-platformer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tips_and_tidbits():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tips-and-tidbits')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_to_purescript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-to-purescript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_todo_list_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-todo-list-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tools_tmbundle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tools.tmbundle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tutorial_cn_old():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tutorial-cn-old')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tutorial_ru():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-tutorial-ru')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_typescript_langserver():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-typescript-langserver')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_unit_testing_with_mocha():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-unit-testing-with-mocha')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_videos_ru_2018():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-videos-ru-2018')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_web():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-web')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_web_srv():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-web-srv')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_winwheel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-winwheel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_workbook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-workbook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_zh():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript-zh')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_patterns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript.patterns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_tmbundle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript.tmbundle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript101():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript101')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript5_mini():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript5-mini')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript6_examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript6_examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_computer_science_exercises():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript_computer_science_exercises')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_curriculum():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript_curriculum')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascript_playground():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascript_playground')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascriptcookbook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascriptcookbook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascripting():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascripting')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascriptstuff_db():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascriptstuff-db')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_javascriptvisualizer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'javascriptvisualizer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_jerryscript():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'jerryscript')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_jest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jest_webdriver():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jest-webdriver')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jinja():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jinja')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jint():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jint')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jison():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jison')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_johnny_five():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'johnny-five')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_joint():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'joint')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_joplin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'joplin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_joshfire_framework():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'joshfire-framework')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jotted():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jotted')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jqm_pagination():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jqm-pagination')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jqmobile_metro_theme():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jqmobile-metro-theme')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_approach():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-approach')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_countdown():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-countdown')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_deserialize():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-deserialize')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_facebook_multi_friend_selector():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-facebook-multi-friend-selector')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_fastLiveFilter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-fastLiveFilter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_form_builder_plugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-form-builder-plugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_html5_upload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-html5-upload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_inlog():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-inlog')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_intelligist():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-intelligist')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_lightbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-lightbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_pjax():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-pjax')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_postmessage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-postmessage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_requestAnimationFrame():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-requestAnimationFrame')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_scrollintoview():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-scrollintoview')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_serialize_object():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-serialize-object')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_simple_slider():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-simple-slider')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_timepicker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-timepicker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_timing():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-timing')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_video_extend():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery-video-extend')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_backgroundSize_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.backgroundSize.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_diamonds_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.diamonds.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_entwine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.entwine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_eventsource():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.eventsource')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_inlineedit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.inlineedit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_resizeend():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.resizeend')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_selection():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.selection')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_serialScroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.serialScroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_snapscroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.snapscroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jquery_tweetable_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jquery.tweetable.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jqueryrotate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jqueryrotate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jrac():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jrac')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_assignments():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-assignments')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_base64():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-base64')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_beautify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-beautify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_bits():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-bits')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_by_examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-by-examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_cookie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-cookie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_git():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-git')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_iso8601():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-iso8601')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_mind():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-mind')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_mindmap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-mindmap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_must_watch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-must-watch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_plugin_circliful():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-plugin-circliful')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_projects():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-projects')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_stack_from_scratch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-stack-from-scratch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_testing_boilerplates():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-testing-boilerplates')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_training():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-training')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_vuln_db():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-vuln-db')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_yaml():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js-yaml')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js_org():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js.org')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_js2coffee():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'js2coffee')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsPDF():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsPDF')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsStudy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsStudy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsTag():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsTag')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsandbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsandbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsbeautify_for_chrome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsbeautify-for-chrome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsbin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsbin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jscodeshift():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jscodeshift')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsctags():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsctags')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsdiff():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsdiff')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsdoc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsdoc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsduck():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsduck')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsep():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsep')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsfeat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsfeat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsfuck():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsfuck')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsgif():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsgif')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jslogo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jslogo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsmind():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsmind')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsmpeg():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsmpeg')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsmvc_pres():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsmvc-pres')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsnes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsnes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_json_server():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'json-server')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsondiffpatch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsondiffpatch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsonpath():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsonpath')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jspm_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jspm-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsqrcode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsqrcode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsrepl():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsrepl')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsrt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsrt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jstat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jstat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jstorm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jstorm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jstutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jstutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jsvu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jsvu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jszip():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jszip')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_juggernaut_plugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'juggernaut_plugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jumly():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jumly')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jungle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jungle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_just_not_sorry():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'just-not-sorry')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_jxcore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'jxcore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kademlia():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kademlia')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kadoh():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kadoh')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_karma():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'karma')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kbengine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kbengine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kd_tree_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kd-tree-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kept():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kept')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ketchup_plugin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ketchup-plugin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_keycodes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'keycodes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kickstart_meteor_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kickstart-meteor-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kickstart_meteor_react_router():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kickstart-meteor-react-router')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kickup():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kickup')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kinetic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kinetic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kitchensink():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kitchensink')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kiwi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kiwi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kline():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kline')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kmdjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kmdjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ko_javascript_info():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ko.javascript.info')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_koa():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'koa')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_koa_middlewares():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'koa-middlewares')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_koa_project_tpl():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'koa-project-tpl')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_koa_proxy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'koa-proxy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_koa_resource_router():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'koa-resource-router')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kopi_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kopi.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kotojs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kotojs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kratko_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kratko.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kss_rails():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kss-rails')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_kubernetes_engine_samples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'kubernetes-engine-samples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_es6_javascript_koans():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-es6-javascript-koans')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_advanced_algorithms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-advanced-algorithms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_basic_algorithms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-basic-algorithms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_chronometer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-chronometer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_clue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-clue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_functions_and_arrays():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-functions-and-arrays')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_greatest_movies():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-greatest-movies')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_koans():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-koans')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_memory_game():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-memory-game')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lab_javascript_vikings():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lab-javascript-vikings')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_labelmask():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'labelmask')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ladda_angular():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ladda-angular')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lambda_complex():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lambda-complex')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lambda_packager():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lambda-packager')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_language_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'language-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_laraflat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'laraflat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_laravel_blade_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'laravel-blade-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_laravel_jsvalidation():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'laravel-jsvalidation')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_layui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'layui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lazyload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lazyload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lazypipe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lazypipe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lazysizes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lazysizes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_leapjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'leapjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_learn_fullstack_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'learn-fullstack-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_learn_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'learn-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_learnGitBranching():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'learnGitBranching')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lectric():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lectric')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_leetcode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'leetcode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_leetcode_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'leetcode-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lell():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lell')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lerna():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lerna')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_less_js_middleware():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'less.js-middleware')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lets_code_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lets_code_javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_letsrate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'letsrate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_libcanvas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'libcanvas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_libsignal_protocol_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'libsignal-protocol-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_libv8():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'libv8')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_libxmljs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'libxmljs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lifxjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lifxjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lightgallery_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lightgallery.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lighthouse():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lighthouse')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lightstep_tracer_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lightstep-tracer-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_limestone():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'limestone')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_linq():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'linq')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_liquid_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'liquid.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_liquidfun():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'liquidfun')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_listloading():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'listloading')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_live_cljs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'live-cljs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_live_log_analyzer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'live-log-analyzer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_livecss():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'livecss')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lively():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lively')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lmd():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lmd')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_loadrunner():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'loadrunner')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_localForage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'localForage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lodash():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lodash')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_log_sys():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'log-sys')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lookforward():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lookforward')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lottie_web():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lottie-web')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_loupe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'loupe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_love_webplayer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'love-webplayer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lrInfiniteScroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lrInfiniteScroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lvlDragDrop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lvlDragDrop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_lz_string():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'lz-string')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mach():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mach')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_machine_learning_for_software_engineers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'machine-learning-for-software-engineers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_magic_iterable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'magic-iterable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_magix_inspector():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'magix-inspector')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_magixjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'magixjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mailmao():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mailmao')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_make_me():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'make-me')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_manim():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'manim')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mantra_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mantra-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mantra_sample_blog_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mantra-sample-blog-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_map_stream():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'map-stream')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mapbox_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mapbox.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mapquery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mapquery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_maps_api_for_javascript_examples():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'maps-api-for-javascript-examples')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_markdown_here():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'markdown-here')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_markdown_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'markdown-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_markdown_live():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'markdown-live')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_marked():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'marked')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_markerclustererplus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'markerclustererplus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_marktext():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'marktext')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_marquette():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'marquette')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mastering_modular_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mastering-modular-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_matchmedia_ng():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'matchmedia-ng')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_material():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'material')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_material_theme_appbar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'material-theme-appbar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_material_ui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'material-ui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_material_ui_vue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'material-ui-vue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_materialize():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'materialize')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_materials():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'materials')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mathjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mathjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_matrix_react_sdk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'matrix-react-sdk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_md2react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'md2react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mechanic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mechanic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meeting_ticker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meeting-ticker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_megamanjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'megamanjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_melonJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'melonJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_memdiff():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'memdiff')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mermaid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mermaid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_chat_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-chat-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_collection_helpers():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-collection-helpers')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_ddp_analyzer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-ddp-analyzer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_pg():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-pg')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_polymer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-polymer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_react_layout():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-react-layout')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_react_router_ssr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-react-router-ssr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_rethinkdb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-rethinkdb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_spin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-spin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_tupperware():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-tupperware')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_typeahead():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-typeahead')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_vue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-vue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_webpack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-webpack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_meteor_webpack_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'meteor-webpack-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_metro():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'metro')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_metronome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'metronome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_micro_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'micro-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_microcosm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'microcosm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_midas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'midas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_minimal_gltf_loader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'minimal-gltf-loader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_minimatch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'minimatch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_minwidth_relocate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'minwidth-relocate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mithril_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mithril.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mixpanel_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mixpanel-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ml():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ml')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mobile_packages():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mobile-packages')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mobile_ui_patterns():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mobile-ui-patterns')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mobx():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mobx')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mobx_reactor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mobx-reactor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mocha():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mocha')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modalbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modalbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modelizr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modelizr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modern_backbone_starterkit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modern-backbone-starterkit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modern_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modern-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modulargrid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modulargrid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modulejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modulejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_modules():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'modules')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mojs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mojs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_moment():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'moment')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_monaco_editor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'monaco-editor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mongodb_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mongodb-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mongoose():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mongoose')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mongoose_q():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mongoose-q')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_monocles():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'monocles')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_monorouter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'monorouter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_moobile_core():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'moobile-core')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mootools_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mootools-bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mootools_mobile():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mootools-mobile')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mostly_adequate_guide():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mostly-adequate-guide')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mousetrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mousetrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mout():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mout')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_move_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'move.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_movie_board():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'movie-board')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_movies_javascript_bolt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'movies-javascript-bolt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_moving_things_with_javascript_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'moving-things-with-javascript-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mpvue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mpvue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mr_doc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mr-doc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_msgpack_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'msgpack-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_msgpack_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'msgpack-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_msgpack_lite():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'msgpack-lite')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_msgraph_sdk_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'msgraph-sdk-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mtg_sdk_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mtg-sdk-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mtui_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mtui-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mullet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mullet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_multilevel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'multilevel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_multiline():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'multiline')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_must_watch_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'must-watch-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mustache_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mustache.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_mvi_example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'mvi-example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_napajs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'napajs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_napp_alloy_adapter_restsql():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'napp.alloy.adapter.restsql')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nash():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nash')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_naturalScroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'naturalScroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ndm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ndm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ndu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ndu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nearley():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nearley')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nectarjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nectarjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_neo4j_javascript_driver():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'neo4j-javascript-driver')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_neo4js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'neo4js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_neocortex():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'neocortex')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nerve():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nerve')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_neunode():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'neunode')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_neuron():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'neuron')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_new_relic_boxes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'new-relic-boxes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_newbie_training():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'newbie-training')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_newsmonger():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'newsmonger')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_next_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'next.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ng_classy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ng-classy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ng_simplePagination():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ng-simplePagination')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ng_youtube_embed():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ng-youtube-embed')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ngForce():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ngForce')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ngMeteor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ngMeteor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ngMidwayTester():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ngMidwayTester')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ngVideo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ngVideo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nightmare():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nightmare')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_amf():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-amf')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_cloudfiles():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-cloudfiles')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_codein():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-codein')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_comment_macros():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-comment-macros')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_csswring():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-csswring')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_dbmon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-dbmon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_dronestream():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-dronestream')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_errno():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-errno')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_fast():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-fast')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_google_distance():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-google-distance')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_hashish():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-hashish')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_host():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-host')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_icalendar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-icalendar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_int64():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-int64')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_jscs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-jscs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_jsonwebtoken():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-jsonwebtoken')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_lessons():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-lessons')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_libvirt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-libvirt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_markdown():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-markdown')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_memcache():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-memcache')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_millenium():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-millenium')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_mime():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-mime')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_modules():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-modules')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_mongolian():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-mongolian')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_neo4j_template():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-neo4j-template')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_paperboy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-paperboy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_persistence():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-persistence')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_quickcheck():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-quickcheck')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_romulus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-romulus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_rtc_peer_connection():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-rtc-peer-connection')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_serialport():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-serialport')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_tar_gz():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-tar.gz')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_term_list():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-term-list')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_twilio():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-twilio')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_xml():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-xml')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_xml2js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-xml2js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_ytdl_core():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node-ytdl-core')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_dbslayer_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node.dbslayer.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodeRunner():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodeRunner')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_node_alipay():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'node_alipay')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodebestpractices():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodebestpractices')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodecms():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodecms')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodejs_intro():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodejs-intro')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodemailer_smtp_transport():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodemailer-smtp-transport')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodember():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodember')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodemon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodemon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_noderce():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'noderce')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodeshot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodeshot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodewiki():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodewiki')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nodrr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nodrr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_noflo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'noflo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_normalizr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'normalizr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_normalizr_immutable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'normalizr-immutable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_notes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'notes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_notifer_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'notifer.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nprogress():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nprogress')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nssocket():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nssocket')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nucleus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nucleus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nude_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nude.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_numeric():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'numeric')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_numjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'numjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_numscrubberjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'numscrubberjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nutella_scrape():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nutella-scrape')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nuxt_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nuxt.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nw_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nw.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nwmatcher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nwmatcher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nya_bootstrap_select():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nya-bootstrap-select')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nylas_mail():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nylas-mail')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_nyroModal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'nyroModal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_o_O():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'o_O')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_obey():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'obey')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_objgrep():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'objgrep')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ocrad_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ocrad.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_octotree():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'octotree')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_odoo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'odoo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_olcPixelGameEngine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'olcPixelGameEngine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_on_media_query():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'on-media-query')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_onejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'onejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_opal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'opal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_open_bounty():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'open-bounty')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_open_source_search_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'open-source-search-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_opencvjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'opencvjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_openpgpjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'openpgpjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_opentracing_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'opentracing-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_opentype_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'opentype.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_orb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'orb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_orbited2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'orbited2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_orca():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'orca')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_oriento():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'oriento')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_osgjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'osgjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_otto():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'otto')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_over_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'over-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_owt_client_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'owt-client-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_p2_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'p2.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_paho_mqtt_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'paho.mqtt.javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pangu_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pangu.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_parallax():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'parallax')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_parcel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'parcel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pareidoloop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pareidoloop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_parse_angular_patch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'parse-angular-patch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_parse_server():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'parse-server')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_particle_excess_demo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'particle-excess-demo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_particles_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'particles.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_passport():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'passport')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pastalog():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pastalog')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pathmenu_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pathmenu.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pavlov():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pavlov')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pdf_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pdf.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pdfkit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pdfkit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pdfmake():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pdfmake')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_peerdium():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'peerdium')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pegjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pegjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_percolatestudio_com():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'percolatestudio.com')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_perk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'perk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_permission_site():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'permission.site')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_phantom_jasmine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'phantom-jasmine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_phantom_render_stream():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'phantom-render-stream')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_phaser():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'phaser')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_phoneformat_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'phoneformat.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_phonegap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'phonegap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_phonegap_desktop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'phonegap-desktop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_photobooth_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'photobooth-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_picard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'picard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pin_cushion():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pin-cushion')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pipelines_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pipelines-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pipelines_javascript_docker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pipelines-javascript-docker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pithy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pithy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pixastic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pixastic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pixel_picker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pixel-picker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pl():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pl')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_placeholder():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'placeholder')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_placeholder_enhanced():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'placeholder-enhanced')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_planck_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'planck.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_plexus_form():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'plexus-form')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_plotly_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'plotly.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ploy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ploy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_plv8():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'plv8')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_plyr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'plyr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pm2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pm2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pm2_webshell():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pm2-webshell')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pnotify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pnotify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pocketsphinx_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pocketsphinx.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_poi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'poi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_polycrypt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'polycrypt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_polyfill():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'polyfill')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_polyfill_webcomponents():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'polyfill-webcomponents')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_polymer_dev():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'polymer-dev')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_polymer_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'polymer-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_popcorntime_smarttv():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'popcorntime-smarttv')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_popmotion():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'popmotion')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_popper_core():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'popper-core')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_post_forking():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'post-forking')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_postcss():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'postcss')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_postcss_icss_values():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'postcss-icss-values')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_postmark_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'postmark.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pq():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pq')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_practical_modern_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'practical-modern-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pre3d():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pre3d')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_preact():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'preact')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_prepack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'prepack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_prettier():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'prettier')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_prettyCheckable():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'prettyCheckable')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_prismic_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'prismic-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_processing_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'processing-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_profvis():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'profvis')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_project_guidelines():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'project-guidelines')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_projector():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'projector')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_promises_book():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'promises-book')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_promptu_menu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'promptu-menu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_propel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'propel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_protobuf_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'protobuf.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_protographql():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'protographql')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_prototype():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'prototype')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_proxyquireify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'proxyquireify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pug():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pug')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pull_to_reload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pull-to-reload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pulse():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pulse')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pumpify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pumpify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_puppeteer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'puppeteer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_purescript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'purescript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pusher_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pusher-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_put_selector():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'put-selector')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pynYNAB():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pynYNAB')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_pypyjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'pypyjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_python_vs_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'python-vs-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_q():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'q')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_qooxdoo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'qooxdoo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_qr_scanner():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'qr-scanner')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_qrcodejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'qrcodejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_qss():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'qss')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_quaggaJS():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'quaggaJS')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_quail():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'quail')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_querystring():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'querystring')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_queuer_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'queuer.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_quick_javascript_switcher():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'quick-javascript-switcher')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_quick_ng_repeat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'quick-ng-repeat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_quickblox_javascript_sdk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'quickblox-javascript-sdk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_quill():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'quill')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_qunit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'qunit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_r_token():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'r-token')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_r2d2b2g():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'r2d2b2g')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rabbot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rabbot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_racket():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'racket')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_radium_grid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'radium-grid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ragadjust():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ragadjust')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rainbow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rainbow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ramda():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ramda')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_raphael():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'raphael')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_raphael_svg_import():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'raphael-svg-import')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_raphael_serialize():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'raphael.serialize')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_raphy_charts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'raphy-charts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ratchet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ratchet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rave():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rave')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_razzle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'razzle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rd3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rd3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reD3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reD3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_bootstrap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-bootstrap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_canvas():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-canvas')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_component_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-component-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_dapp_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-dapp-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_decorators():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-decorators')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_developer_roadmap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-developer-roadmap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_echarts_modules():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-echarts-modules')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_flight():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-flight')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_fullstack_skeleton():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-fullstack-skeleton')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_hooks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-hooks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_hot_loader_loader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-hot-loader-loader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_imation():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-imation')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_inline_grid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-inline-grid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_intercom():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-intercom')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_javascript_to_typescript_transform():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-javascript-to-typescript-transform')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_json_editor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-json-editor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_lightning_design_system():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-lightning-design-system')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_look():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-look')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_magician():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-magician')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_modules():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-modules')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_motion():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-motion')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_clean_form():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-clean-form')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_complex_nav():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-complex-nav')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_elements():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-elements')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_gift_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-gift-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_hot_redux_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-hot-redux-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_loading_container():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-loading-container')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_refresh_infinite_listview():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-refresh-infinite-listview')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_selectablesectionlistview():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-selectablesectionlistview')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_smart_scroll_view():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-smart-scroll-view')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_swiper_animated():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-swiper-animated')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_tabbar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-tabbar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_web():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-web')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_native_webview_bridge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-native-webview-bridge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_organism():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-organism')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_page_transitions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-page-transitions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_pagify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-pagify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_pivot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-pivot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_pledge():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-pledge')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_redux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-redux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_redux_example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-redux-example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_router():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-router')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_ruby_china():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-ruby-china')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_select():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-select')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_semantify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-semantify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_showroom_client():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-showroom-client')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_spring():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-spring')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_stampit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-stampit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_starter_kit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-starter-kit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_static_plate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-static-plate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_stylesheet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-stylesheet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_testing_mocha_jsdom():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-testing-mocha-jsdom')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_time():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-time')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_transform_catch_errors():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-transform-catch-errors')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_tutorial_todos():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-tutorial-todos')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_validation_mixin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-validation-mixin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_virtualized():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-virtualized')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_way_getting_started():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-way-getting-started')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_way_immutable_flux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-way-immutable-flux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_webpack_example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-webpack-example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_react_with_hooks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'react-with-hooks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reactcards():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reactcards')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_readium_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'readium-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_real_world_javascript_interview_questions():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'real-world-javascript-interview-questions')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_really_simple_color_picker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'really-simple-color-picker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_realtime_playground():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'realtime-playground')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_realworld():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'realworld')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rebound_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rebound-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reclare():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reclare')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_recompose():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'recompose')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_red_dwarf():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'red-dwarf')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redash():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redash')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redis_node():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redis-node')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redmine_lightbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redmine_lightbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_act_async():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-act-async')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_await():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-await')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_easy_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-easy-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_fractal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-fractal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_friendlist_demo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-friendlist-demo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_react_navigation_demos():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-react-navigation-demos')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_requests():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-requests')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_saga():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-saga')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_saga_tester():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-saga-tester')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_redux_webpack_es6_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'redux-webpack-es6-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_refluxjs_todo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'refluxjs-todo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_refraction():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'refraction')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_refunk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'refunk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_registry():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'registry')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_regression_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'regression-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_relate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'relate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_relay():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'relay')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_relay_sink():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'relay-sink')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rellax():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rellax')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_remtail():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'remtail')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_render_markdown_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'render-markdown-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_replpad():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'replpad')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reporting_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reporting-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_request():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'request')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_require_analyzer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'require-analyzer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_requirejs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'requirejs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_requirejs_library():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'requirejs-library')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rereduce():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rereduce')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reselect():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reselect')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_resin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'resin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_resourceful():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'resourceful')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_responsive_mockups():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'responsive_mockups')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rest_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rest.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_restmvc_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'restmvc.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_resume_github_com():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'resume.github.com')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reveal_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reveal.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_reverse_engineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'reverse-engineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_revue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'revue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rfc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rfc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_riak_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'riak-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rickshaw():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rickshaw')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_riot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'riot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_riot_isomorphic():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'riot-isomorphic')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_riotjs_startkit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'riotjs-startkit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rndr_me():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rndr.me')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rocambole():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rocambole')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rollerblade():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rollerblade')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


#  def test_repos_rollup():
#      path_name = os.path.join(constants.seeds_dir, 'repos', 'rollup')
#      multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)
 

# def test_repos_rome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_roslibjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'roslibjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rts():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rts')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ru_javascript_info():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ru.javascript.info')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ruby_javascript_data_viz():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ruby_javascript_data_viz')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_run_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'run-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_runloop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'runloop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rxdb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rxdb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_rxjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'rxjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_s3upload_coffee_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 's3upload-coffee-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sa_sdk_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sa-sdk-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sailng():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sailng')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sails():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sails')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sails_auth():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sails-auth')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sails_hook_autoreload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sails-hook-autoreload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sails_react_example():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sails-react-example')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sammy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sammy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sample_arti():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sample-arti')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sample_hapi_rest_api():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sample-hapi-rest-api')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sample_app_rails_4():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sample_app_rails_4')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_san():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'san')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sanctuary_def():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sanctuary-def')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sass_color_picker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sass-color-picker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_satisfy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'satisfy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_savepublishing():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'savepublishing')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sc_crud_sample():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sc-crud-sample')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scala_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scala-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scooch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scooch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scoreunder():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scoreunder')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scotch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scotch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_screencap():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'screencap')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_screw_unit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'screw-unit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scribbletune():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scribbletune')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_script_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'script.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scriptular():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scriptular')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scrollport_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scrollport-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_scrollreveal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'scrollreveal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_search_source():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'search-source')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_searx():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'searx')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_select2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'select2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sennajs_com():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sennajs.com')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sense_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sense-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sense_old():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sense_old')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sentry_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sentry-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sequelize():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sequelize')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_serialize_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'serialize-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_serverless():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'serverless')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_services():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'services')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_services_engineering():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'services-engineering')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_servo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'servo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_servo_shell():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'servo-shell')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shaka_player():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shaka-player')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shapado():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shapado')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shape_form():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shape-form')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shapesmith():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shapesmith')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sharp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sharp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sheetjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sheetjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sherlogjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sherlogjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shift_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shift-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_short_and_sweet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'short-and-sweet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_shower():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'shower')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sigma_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sigma.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_simpl():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'simpl')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_simple_frontend_boilerplate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'simple-frontend-boilerplate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_simple_statistics():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'simple-statistics')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_simpleCRM():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'simpleCRM')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_simpledb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'simpledb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sinon():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sinon')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sixflix():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sixflix')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sizzle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sizzle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sjcl():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sjcl')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sketch_data_studio():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sketch-data-studio')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sketch_relabel_button():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sketch-relabel-button')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sketch_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sketch.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_skills_based_javascript_intro_to_flow_control_bootcamp_prep_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'skills-based-javascript-intro-to-flow-control-bootcamp-prep-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_skills_based_javascript_intro_to_flow_control_js_intro_000():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'skills-based-javascript-intro-to-flow-control-js-intro-000')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_skrollr_decks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'skrollr-decks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_skulpt():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'skulpt')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_slack_news():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'slack-news')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_slate():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'slate')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_slick():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'slick')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_slush_angular():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'slush-angular')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_smart_contract():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'smart_contract')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_smile():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'smile')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_smokescreen():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'smokescreen')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_smokestack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'smokestack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_smoosh():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'smoosh')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_snabbt_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'snabbt.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_snippets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'snippets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_snowplow_javascript_tracker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'snowplow-javascript-tracker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_soca():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'soca')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_social_engineer_toolkit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'social-engineer-toolkit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_socket_io():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'socket.io')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_socket_io_titanium():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'socket.io-titanium')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_socketcluster_client():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'socketcluster-client')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sockjs_client():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sockjs-client')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sodajs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sodajs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_solidityx_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'solidityx-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_soundcloud_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'soundcloud-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_space_tweet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'space-tweet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spacedrop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spacedrop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spark():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spark')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sparky():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sparky')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spazcore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spazcore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_speak_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'speak.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_specter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'specter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spectrum():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spectrum')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_speech_javascript_sdk():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'speech-javascript-sdk')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_speed_monitor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'speed-monitor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spicetify_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spicetify-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spine_todos():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spine.todos')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spm2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spm2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_spmx():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'spmx')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sqip():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sqip')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sql_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sql.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_squel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'squel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_srcset_polyfill():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'srcset-polyfill')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stackedit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stackedit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_standard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'standard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_starter_javascript_exercicios():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'starter-javascript-exercicios')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stat_distributions_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stat-distributions-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stats_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stats.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_statsd():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'statsd')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_steal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'steal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_steamSummerMinigame():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'steamSummerMinigame')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stellarium_web_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stellarium-web-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_step_by_step_frontend():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'step-by-step-frontend')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stimulus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stimulus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stochator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stochator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stockfish_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stockfish.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_storybook_addon_jest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'storybook-addon-jest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_storybook_addon_knobs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'storybook-addon-knobs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_storyshots():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'storyshots')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stp_pediff():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stp.pediff')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_strapi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'strapi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_strapi_sdk_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'strapi-sdk-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stream_handbook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stream-handbook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stream_spec():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stream-spec')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_streamgraph_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'streamgraph.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_streamie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'streamie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_strftime():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'strftime')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stride():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stride')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_string_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'string.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stripe_meteor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stripe-meteor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_strman():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'strman')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_strong_pm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'strong-pm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_structuring_backbone_with_requirejs_and_marionette():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'structuring-backbone-with-requirejs-and-marionette')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stuhome():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stuhome')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_styled_components():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'styled-components')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_styled_theme():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'styled-theme')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_styler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'styler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_stylis_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'stylis.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sublime_javascript_snippets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sublime-javascript-snippets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sublime_text_refactor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sublime-text-refactor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_substance_text():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'substance-text')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_substituteteacher_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'substituteteacher.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_suggest():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'suggest')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sunnybaby():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sunnybaby')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_superagent():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'superagent')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_supergrep():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'supergrep')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_superherojs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'superherojs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_supertest_as_promised():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'supertest-as-promised')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_superui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'superui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_superviews_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'superviews.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_survey_library():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'survey-library')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_svelte():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'svelte')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_svgo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'svgo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_swagger_ui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'swagger-ui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_swaggerize_express():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'swaggerize-express')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sweet_core():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sweet-core')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sweet_justice():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sweet-justice')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sweetalert():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sweetalert')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_swf2js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'swf2js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_swig():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'swig')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_swiper():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'swiper')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_symbol_sdk_typescript_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'symbol-sdk-typescript-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_sync_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'sync-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_systemjs_seed():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'systemjs-seed')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_syze():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'syze')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_t1_runtime():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 't1-runtime')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tEmbO():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tEmbO')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_taberareloo():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'taberareloo')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tabler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tabler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tabulator():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tabulator')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tap_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tap.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tapchat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tapchat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_taro():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'taro')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_task_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'task.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_teamchatviz():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'teamchatviz')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tech_interview_handbook():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tech-interview-handbook')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tedit():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tedit')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_telepat_api():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'telepat-api')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_template_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'template.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_template7():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'template7')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_templayed_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'templayed.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_term_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'term.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_terminus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'terminus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tern_meteor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tern-meteor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_terrain():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'terrain')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_terse_webpack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'terse-webpack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tesserace():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tesserace')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tesseract():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tesseract')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tesseract_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tesseract.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_testable_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'testable-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_testing_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'testing-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_text_mask():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'text-mask')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tfjs_core():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tfjs-core')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_the_javascript_curriculum():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'the-javascript-curriculum')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_the_super_tiny_compiler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'the-super-tiny-compiler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thedaywefightback_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thedaywefightback.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thejsway():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thejsway')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_themoviedb_javascript_library():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'themoviedb-javascript-library')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thingiview_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thingiview.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thinky():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thinky')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thorax_seed():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thorax-seed')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_three_orbit_controls():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'three-orbit-controls')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_three_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'three.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thumbbot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thumbbot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thumbd():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thumbd')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_thunderbird():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'thunderbird')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tic_tac_toe_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tic-tac-toe-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tile5():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tile5')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_timeframe():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'timeframe')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_timezone():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'timezone')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tiny_slider():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tiny-slider')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tinymce_rails_imageupload():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tinymce-rails-imageupload')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tip_cards():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tip_cards')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tips():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tips')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tire():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tire')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_titanium_facebook_slide_menu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'titanium-facebook-slide-menu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_titanium_developer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'titanium_developer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_titanium_mobile():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'titanium_mobile')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tmlib_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tmlib.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_toastr():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'toastr')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_todomvc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'todomvc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_toe_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'toe.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_token_based_auth_frontend():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'token-based-auth-frontend')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tonal():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tonal')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_topup():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'topup')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tor_fingerprint():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tor-fingerprint')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_touche():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'touche')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tpl_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tpl.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tr8n():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tr8n')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_traceur_compiler():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'traceur-compiler')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_transducers_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'transducers-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_transformer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'transformer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_travel_RN():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'travel-RN')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tree_grid_directive():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tree-grid-directive')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_trek():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'trek')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_trello_calendar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'trello-calendar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_trial_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'trial-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_trilha_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'trilha-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_trophymanager():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'trophymanager')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ttf_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ttf.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tufte_graph():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tufte-graph')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tui_calendar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tui.calendar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tumblr_downloader():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tumblr-downloader')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_turbine_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'turbine.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_turbulenz_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'turbulenz_engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_turf():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'turf')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_tween_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'tween.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_twostroke():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'twostroke')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_twss_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'twss.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_typeahead_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'typeahead.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_typed_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'typed.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_typeofnan_javascript_quizzes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'typeofnan-javascript-quizzes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_typist_jquery():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'typist-jquery')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uBlock():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uBlock')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ud549():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ud549')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ui_progress_bar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ui-progress-bar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ui_tinymce():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ui-tinymce')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uiji():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uiji')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uilayer():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uilayer')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_underscore():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'underscore')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_underscore_inflection():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'underscore.inflection')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_underscore_string():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'underscore.string')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_understanding_npm():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'understanding-npm')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unexpected_react():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unexpected-react')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unexpected_react_shallow():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unexpected-react-shallow')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uni_app():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uni-app')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unicorn():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unicorn')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unify():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unify')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_universal_react_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'universal-react-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_universal_redux_template():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'universal-redux-template')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_university():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'university')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unprecedented_midwife():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unprecedented-midwife')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unsplash_source_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unsplash-source-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_unused_My_Wallet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'unused-My-Wallet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uppy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uppy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uri_templates():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uri-templates')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_use_amd():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'use-amd')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_utils():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'utils')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_uuid():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'uuid')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v2ex_ext():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v2ex.ext')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v3_utility_library():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v3-utility-library')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v7():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v7')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v8():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v8')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v86():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v86')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v8eval():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v8eval')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v8js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v8js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v8n():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v8n')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_v8pp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'v8pp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vagueTime_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vagueTime.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_validate_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'validate.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_validator_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'validator.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vant_weapp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vant-weapp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vector_river_map():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vector-river-map')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vektor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vektor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_velocity():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'velocity')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_velositey():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'velositey')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_veria():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'veria')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_verlet_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'verlet-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_video_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'video.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_viewer_javascript_tutorial():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'viewer-javascript-tutorial')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_viewer_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'viewer.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_viewerjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'viewerjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vim_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vim-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vim_recipes():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vim-recipes')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vim_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vim.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vivus():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vivus')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vm_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vm.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_voca():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'voca')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vogue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vogue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_voie():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'voie')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vot_ar():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vot.ar')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_voxel_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'voxel-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_voxelengine3():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'voxelengine3')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vscode_es7_javascript_react_snippets():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vscode-es7-javascript-react-snippets')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vscode_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vscode-javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vticker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vticker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vtree():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vtree')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vts_browser_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vts-browser-js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_autocomplete():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-autocomplete')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_cli():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-cli')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_clip():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-clip')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_devtools():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-devtools')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_file_upload_component():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-file-upload-component')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_mini_shop():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-mini-shop')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_region_picker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-region-picker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_router():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-router')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_server():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-server')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_smart_table():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-smart-table')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vue_starter():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vue-starter')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vuepress():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vuepress')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vuera():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vuera')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vuex():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vuex')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_vuln_javascript():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'vuln_javascript')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wagn():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wagn')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_walkabout_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'walkabout.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wax():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wax')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wdui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wdui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_weapp_session():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'weapp-session')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_web_bundle():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'web-bundle')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_web3_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'web3.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webRTCCopy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webRTCCopy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webSlide():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webSlide')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webkit_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webkit.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack_MultiplePage():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack-MultiplePage')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack_chrome_extension():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack-chrome-extension')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack_dashboard():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack-dashboard')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack_messages():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack-messages')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack_serve():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack-serve')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpack_uglify_parallel():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpack-uglify-parallel')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webpacker():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webpacker')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webservice_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webservice.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_webtorrent():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'webtorrent')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wechat_helper():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wechat-helper')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_weex_learning():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'weex-learning')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wekan():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wekan')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wepy():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wepy')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_weui_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'weui.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wheel_menu():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wheel-menu')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_whiskey():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'whiskey')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_whitewater_mobile_video():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'whitewater-mobile-video')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wikifetch():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wikifetch')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wind():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wind')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wink():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wink')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_winston():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'winston')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_with_react_hooks():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'with-react-hooks')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wizardry():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wizardry')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_workbox():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'workbox')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_workshop_js_funcional_free():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'workshop-js-funcional-free')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wp_calypso():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wp-calypso')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wpilot():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wpilot')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_ws():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'ws')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wtfjs():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wtfjs')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wujb():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wujb')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wx():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wx')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wxapp_devFrame():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wxapp-devFrame')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wysihat():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wysihat')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wysihat_engine():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wysihat-engine')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_wysiwyg_editor():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'wysiwyg-editor')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_x_spreadsheet():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'x-spreadsheet')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xdomain():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xdomain')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xiaotiantian():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xiaotiantian')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xjst():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xjst')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xkcd_pixels():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xkcd-pixels')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xmpp_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xmpp.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xregexp():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xregexp')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xscroll():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xscroll')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xssor2():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xssor2')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xto():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xto')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_xui():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'xui')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_yapi():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'yapi')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_yarn():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'yarn')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_youkuhtml5playerbookmark():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'youkuhtml5playerbookmark')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_yours_bitcoin():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'yours-bitcoin')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_yuidoc():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'yuidoc')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_z():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'z')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_zelect():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'zelect')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_zeroclickinfo_goodies():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'zeroclickinfo-goodies')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_zethos():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'zethos')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_zh_javascript_info():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'zh.javascript.info')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_zip_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'zip.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


# def test_repos_zone_js():
#     path_name = os.path.join(constants.seeds_dir, 'repos', 'zone.js')
#     multicall.multicall_directories(path_name, fuzzer='radamsa', validator=validate)


