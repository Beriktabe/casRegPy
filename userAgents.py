from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, HardwareType, SoftwareType

operating_systems = [OperatingSystem.ANDROID.value, OperatingSystem.IOS.value]
hardware_types = [HardwareType.MOBILE__PHONE.value, HardwareType.MOBILE.value]
software_types = [SoftwareType.BROWSER__IN_APP_BROWSER.value, SoftwareType.WEB_BROWSER.value]

def getUsrAgent() -> str: #todo later

    user_agent_rotator = UserAgent(operating_systems=operating_systems, hardware_types=hardware_types, software_types=software_types)

    return user_agent_rotator.get_random_user_agent()