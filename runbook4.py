from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def pull_structed_data(task):
    version_result = task.run(task=send_command, command="show version")
    task.host ["facts"] = version_result.scrapli_response.genie_parse_output()
    print(task.host["facts"])

results = nr.run(task=pull_structed_data)

# print_result(results)