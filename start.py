import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler

from infi.devicemanager import DeviceManager, functions

stylus_friendly_name = 'Surface Slim Pen 2'
connected_status_guid = '83DA6326-97A6-4088-9453-A1923F573B290F000000'
touchscreen_device_name = '*触摸屏*'
check_interval_seconds = 5

dm = DeviceManager()
dm.root.rescan()
devices = dm.all_devices
device = None
for device_ in devices:
    if device_.has_property('friendly_name') and stylus_friendly_name in device_.friendly_name:
        device = device_
        break


if device is None:
    raise Exception('Device not found')


guid = None


with device._open_handle() as handle:
    dis, devinfo = handle
    guid_list = functions.SetupDiGetDevicePropertyKeys(dis, devinfo)
    for guid_ in guid_list:
        if functions.guid_to_pretty_string(guid_) == connected_status_guid:
            guid = guid_
            break


if guid is None:
    raise Exception('GUID not found')


def get_device_status():
    status_ = device._get_setupapi_property(guid)
    return status_


current_status = get_device_status()


def run_ps(status):
    subprocess.run(
        "powershell -Command Get-PnpDevice | Where-Object {$_.FriendlyName -like '" + touchscreen_device_name + "'} | " +
        ("Enable-PnpDevice" if not status else "Disable-PnpDevice") +
        " -Confirm:$false")


run_ps(current_status)


def check():
    global current_status
    new_status = get_device_status()
    if new_status != current_status:
        run_ps(new_status)
        current_status = new_status


scheduler = BlockingScheduler()
scheduler.add_job(check, 'interval', seconds=5)
scheduler.start()
