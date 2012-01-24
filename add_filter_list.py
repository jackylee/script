#!/usr/bin/python
# Utility for adding unauthorized ip attempt logging to vps
import re
import string
import sys

def extract_ip(log):
   try:
      ip_dict = {};
      pat = re.compile("Failed password.*(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})")
      addr = re.compile("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})")
      with open(log) as handle:
         for line in handle:
            mat = pat.search(line)
            if mat is None:
               continue
            ip = addr.search(mat.group(0))
            if ip is None:
               continue
            if ip.group(0) not in ip_dict:
               ip_dict[ip.group(0)] = 1
            else:
               ip_dict[ip.group(0)] += 1
      return ip_dict
   except:
      print "error occurs during processing log:", sys.exc_info()[0]

def generate_list(log):
   try:
      ip_dict = extract_ip(log)
      handle = open('/tmp/ip.txt', 'w')
      for key in ip_dict:
         handle.write("ssh: " + key+"\n")
      handle.close()
   except:
      print "generate attacking ip address failure:", sys.exc_info()[0]

def print_usage():
   print "version 1.0.0"
   print "add_filter_list [auth.log]"
   print "by jacky.liye@gmail.com"

def cat(name):
   try:
      handle = open(name, 'r')
      for line in handle:
         sys.stdout.write("%s" % line)
      handle.close()
   except:
      print "error occur in open file:", sys.exc_info()[0]

if __name__ == "__main__":
   if len(sys.argv) == 1:
      print_usage()
   else:
      for log in sys.argv[1:]:
         print "processing %s" % log
         generate_list(log)
         cat("/tmp/ip.txt")

