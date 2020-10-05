#Simple Python Script to Show Security IKE & IPSEC in Juniper Junos with Ansible
#Simple Python Script to Add Site to Site VPN Parameter (based on AWS configuration file) in Junos with Ansible
#In this simple script, that should be already have Security Zone configuration for Site to Site VPN Tunnel Interface and External Physical Interface on Junos Configuration
#Feel free to use and modify this code
#Created by Vincensius Yudhistira Lindung Setiyana

import os

cmd_ansible = "ansible-playbook" #create shortcut to call ansible-playbook command
print("Junos Config Task!\n(1) Show IKE\n(2) Show IPSEC\n(3) Add Site to Site VPN IKE Configuration\n(4) Add Site to Site VPN IPSEC Configuration" )
print("--------------------------------------------------------------------\n")
Answer = input("Answer: ")
print("\n")
if Answer == "1":
  ike_peer = input("Enter IKE Peer Address: ")
  with open("junos_show_ike.yml") as r: #open junos_show_ike.yml file with READ fuction
    text = r.read().replace("PEER_ADDRESS", ike_peer) #create variable text and do replace function that match with the "keyword" that we already define on junos_show_ike.yml
  with open("junos_show_ike.yml", "w") as w: #open junos_show_ike.yml file with WRITE fuction, so "keyword" on current junos_show_ike.yml already changed and ready to use for ansible-plabook command 
    w.write(text) #do write fuction
  os.system(cmd_ansible + " junos_show_ike.yml") #call ansible-playbook command then run it for junos_show_ike.yml
  os.system("cp junos_show_ike.txt junos_show_ike.yml") #last step is to "reset" junos_show_ike.yml file with default "keyword"

elif Answer == "2":
  ipsec_vpn_name = input("Enter IPSEC VPN Name: ")
  with open("junos_show_ipsec.yml") as r: #open junos_show_ipsec.yml file with READ fuction
    text = r.read().replace("VPN_NAME", ipsec_vpn_name) #create variable text and do replace function that match with the "keyword" that we already define on junos_show_ipsec.yml
  with open("junos_show_ipsec.yml", "w") as w: #open junos_show_ipsec.yml file with WRITE fuction, so "keyword" on current junos_show_ipsec.yml already changed and ready to use for ansible-plabook command
    w.write(text) #do write fuction
  os.system(cmd_ansible + " junos_show_ipsec.yml") #call ansible-playbook command then run it for junos_show_ipsec.yml
  os.system("cp junos_show_ipsec.txt junos_show_ipsec.yml")  #last step is to "reset" junos_show_ipsec.yml file with default "keyword"

elif Answer == "3":
  print("1. Single IKE Configuration\n2. Multiple IKE Configuration Read From TXT/CSV File\n")
  IKE_Answer = input("Answer: ")
  print("\n")
  if IKE_Answer == "1":
    ike_proposal_name = input("Enter IKE Proposal Name: ")
    ike_policy_name = input("Enter IKE Policy Name: ")
    ike_preshared_key = input("Enter IKE Pre-Shared Key: ")
    ike_gateway_name = input("Enter IKE Gateway Name: ")
    ike_peer_address = input ("Enter IKE Peer Address: ")
    ike_external_interface = input("Enter External Interface for S2S VPN: ")
    with open("add_s2s_ike.yml") as r1:
      text1 = r1.read().replace("IKE_PROPOSAL_NAME", ike_proposal_name)
    with open("add_s2s_ike.yml", "w") as w1:
      w1.write(text1)
    with open("add_s2s_ike.yml") as r2:
      text2 = r2.read().replace("IKE_POLICY_NAME", ike_policy_name)
    with open("add_s2s_ike.yml", "w") as w2:
      w2.write(text2)
    with open("add_s2s_ike.yml") as r3:
      text3 = r3.read().replace("PRESHARED_KEY", ike_preshared_key)
    with open("add_s2s_ike.yml", "w") as w3:
      w3.write(text3)
    with open("add_s2s_ike.yml") as r4:
      text4 = r4.read().replace("IKE_GW_NAME", ike_gateway_name)
    with open("add_s2s_ike.yml", "w") as w4:
      w4.write(text4)
    with open("add_s2s_ike.yml") as r5:
      text5 = r5.read().replace("VPN_PEER_ADDRESS", ike_peer_address)
    with open("add_s2s_ike.yml", "w") as w5:
      w5.write(text5)
    with open("add_s2s_ike.yml") as r6:
      text6 = r6.read().replace("VPN_EXTERNAL_INTERFACE", ike_external_interface)
    with open("add_s2s_ike.yml", "w") as w6:
      w6.write(text6)
    os.system(cmd_ansible + " add_s2s_ike.yml")
    os.system("cp add_s2s_ike.txt add_s2s_ike.yml")

  elif IKE_Answer == "2":
    IKE_Param_List_File = input ("Enter IKE Parameter Configuration list file location: ")
    IKE_Param_List_File_List = open(IKE_Param_List_File, "r")
    for IKE_Param_List in IKE_Param_List_File_List.readlines():
      IKE_Param_List = IKE_Param_List.strip()
      IKE_Param_List_Split = IKE_Param_List.split(",")
      ike_proposal_name = IKE_Param_List_Split[0]
      ike_policy_name = IKE_Param_List_Split[1]
      ike_preshared_key = IKE_Param_List_Split[2]
      ike_gateway_name = IKE_Param_List_Split[3]
      ike_peer_address = IKE_Param_List_Split[4]
      ike_external_interface = IKE_Param_List_Split[5]
      with open("add_s2s_ike.yml") as r1:
        text1 = r1.read().replace("IKE_PROPOSAL_NAME", ike_proposal_name)
      with open("add_s2s_ike.yml", "w") as w1:
        w1.write(text1)
      with open("add_s2s_ike.yml") as r2:
        text2 = r2.read().replace("IKE_POLICY_NAME", ike_policy_name)
      with open("add_s2s_ike.yml", "w") as w2:
        w2.write(text2)
      with open("add_s2s_ike.yml") as r3:
        text3 = r3.read().replace("PRESHARED_KEY", ike_preshared_key)
      with open("add_s2s_ike.yml", "w") as w3:
        w3.write(text3)
      with open("add_s2s_ike.yml") as r4:
        text4 = r4.read().replace("IKE_GW_NAME", ike_gateway_name)
      with open("add_s2s_ike.yml", "w") as w4:
        w4.write(text4)
      with open("add_s2s_ike.yml") as r5:
        text5 = r5.read().replace("VPN_PEER_ADDRESS", ike_peer_address)
      with open("add_s2s_ike.yml", "w") as w5:
        w5.write(text5)
      with open("add_s2s_ike.yml") as r6:
        text6 = r6.read().replace("VPN_EXTERNAL_INTERFACE", ike_external_interface)
      with open("add_s2s_ike.yml", "w") as w6:
        w6.write(text6)
      os.system(cmd_ansible + " add_s2s_ike.yml")
      os.system("cp add_s2s_ike.txt add_s2s_ike.yml")
  else:
    print("Please choose option!")

elif Answer == "4":
  print("1. Single IPSEC Configuration\n2. Multiple IPSEC Configuration Read From TXT/CSV File\n")
  IPSEC_Answer = input("Answer: ")
  print("\n")
  if IPSEC_Answer == "1":
    ipsec_tunnel_address = input("Enter IPSEC Tunnel IP Address: ")
    ipsec_bind_interface = input("Enter IPSEC Tunnel Interface: ")
    ipsec_zone_tunnel_interface = input("Enter Tunnel Interface Security Zone: ")
    ipsec_proposal_name = input("Enter IPSEC Proposal Name: ")
    ipsec_policy_name = input("Enter IPSEC Policy Name: ")
    ipsec_vpn_name = input("Enter IPSEC VPN Name: ")
    ipsec_monitor_address = input ("Enter IPSEC Monitor Address: ")
    ipsec_ike_gateway = input("Enter IKE Gateway Name: ")
    with open("add_s2s_ipsec.yml") as ipsec_r1:
      ipsec_text_replace_1 = ipsec_r1.read().replace("TUNNEL_ADDRESS", ipsec_tunnel_address)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w1:
      ipsec_w1.write(ipsec_text_replace_1)
    with open("add_s2s_ipsec.yml") as ipsec_r2:
      ipsec_text_replace_2 = ipsec_r2.read().replace("IPSEC_BIND_INTERFACE", ipsec_bind_interface)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w2:
      ipsec_w2.write(ipsec_text_replace_2)
    with open("add_s2s_ipsec.yml") as ipsec_r3:
      ipsec_text_replace_3 = ipsec_r3.read().replace("VPN_ZONE_NAME", ipsec_zone_tunnel_interface)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w3:
      ipsec_w3.write(ipsec_text_replace_3)
    with open("add_s2s_ipsec.yml") as ipsec_r4:
      ipsec_text_replace_4 = ipsec_r4.read().replace("IPSEC_PROPOSAL_NAME", ipsec_proposal_name)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w4:
      ipsec_w4.write(ipsec_text_replace_4)
    with open("add_s2s_ipsec.yml") as ipsec_r5:
      ipsec_text_replace_5 = ipsec_r5.read().replace("IPSEC_POLICY_NAME", ipsec_policy_name)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w5:
      ipsec_w5.write(ipsec_text_replace_5)
    with open("add_s2s_ipsec.yml") as ipsec_r6:
      ipsec_text_replace_6 = ipsec_r6.read().replace("IPSEC_VPN_NAME", ipsec_vpn_name)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w6:
      ipsec_w6.write(ipsec_text_replace_6)    
    with open("add_s2s_ipsec.yml") as ipsec_r7:
      ipsec_text_replace_7 = ipsec_r7.read().replace("IPSEC_MONITOR_ADDRESS", ipsec_monitor_address)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w7:
      ipsec_w7.write(ipsec_text_replace_7)
    with open("add_s2s_ipsec.yml") as ipsec_r8:
      ipsec_text_replace_8 = ipsec_r8.read().replace("IPSEC_IKE_GW", ipsec_ike_gateway)
    with open("add_s2s_ipsec.yml", "w") as ipsec_w8:
      ipsec_w8.write(ipsec_text_replace_8)
    os.system(cmd_ansible + " add_s2s_ipsec.yml")
    os.system("cp add_s2s_ipsec.txt add_s2s_ipsec.yml")

  elif IPSEC_Answer == "2":
    IPSEC_Param_List_File = input ("Enter IPSEC Parameter Configuration list file location: ")
    IPSEC_Param_List_File_List = open(IPSEC_Param_List_File, "r")
    for IPSEC_Param_List in IPSEC_Param_List_File_List.readlines():
      IPSEC_Param_List = IPSEC_Param_List.strip()
      IPSEC_Param_List_Split = IPSEC_Param_List.split(",")
      ipsec_tunnel_address = IPSEC_Param_List_Split[0]
      ipsec_bind_interface = IPSEC_Param_List_Split[1]
      ipsec_zone_tunnel_interface = IPSEC_Param_List_Split[2]
      ipsec_proposal_name = IPSEC_Param_List_Split[3]
      ipsec_policy_name = IPSEC_Param_List_Split[4]
      ipsec_vpn_name = IPSEC_Param_List_Split[5]
      ipsec_monitor_address = IPSEC_Param_List_Split[6]
      ipsec_ike_gateway = IPSEC_Param_List_Split[7]
      with open("add_s2s_ipsec.yml") as ipsec_r1:
        ipsec_text_replace_1 = ipsec_r1.read().replace("TUNNEL_ADDRESS", ipsec_tunnel_address)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w1:
        ipsec_w1.write(ipsec_text_replace_1)
      with open("add_s2s_ipsec.yml") as ipsec_r2:
        ipsec_text_replace_2 = ipsec_r2.read().replace("IPSEC_BIND_INTERFACE", ipsec_bind_interface)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w2:
        ipsec_w2.write(ipsec_text_replace_2)
      with open("add_s2s_ipsec.yml") as ipsec_r3:
        ipsec_text_replace_3 = ipsec_r3.read().replace("VPN_ZONE_NAME", ipsec_zone_tunnel_interface)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w3:
        ipsec_w3.write(ipsec_text_replace_3)
      with open("add_s2s_ipsec.yml") as ipsec_r4:
        ipsec_text_replace_4 = ipsec_r4.read().replace("IPSEC_PROPOSAL_NAME", ipsec_proposal_name)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w4:
        ipsec_w4.write(ipsec_text_replace_4)
      with open("add_s2s_ipsec.yml") as ipsec_r5:
        ipsec_text_replace_5 = ipsec_r5.read().replace("IPSEC_POLICY_NAME", ipsec_policy_name)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w5:
        ipsec_w5.write(ipsec_text_replace_5)
      with open("add_s2s_ipsec.yml") as ipsec_r6:
        ipsec_text_replace_6 = ipsec_r6.read().replace("IPSEC_VPN_NAME", ipsec_vpn_name)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w6:
        ipsec_w6.write(ipsec_text_replace_6)    
      with open("add_s2s_ipsec.yml") as ipsec_r7:
        ipsec_text_replace_7 = ipsec_r7.read().replace("IPSEC_MONITOR_ADDRESS", ipsec_monitor_address)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w7:
        ipsec_w7.write(ipsec_text_replace_7)
      with open("add_s2s_ipsec.yml") as ipsec_r8:
        ipsec_text_replace_8 = ipsec_r8.read().replace("IPSEC_IKE_GW", ipsec_ike_gateway)
      with open("add_s2s_ipsec.yml", "w") as ipsec_w8:
        ipsec_w8.write(ipsec_text_replace_8)
      os.system(cmd_ansible + " add_s2s_ipsec.yml")
      os.system("cp add_s2s_ipsec.txt add_s2s_ipsec.yml")

  else:
      print("Please choose option!")

else:
  print("Please choose option!")

#Vincensius Yudhistira Lindung Setiyana | VYLS Project 2020#
