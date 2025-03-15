# Certificates {: .fixme}

<p id="terms"></p>

Run `RERUN.sh` to:

1.  Create CA key and cert
2.  Create server key and cert
3.  Sign server CSR with CA key
4.  Run Python server
5.  Wait for it to listen on port 1443
6.  Run Python client using `requests`
7.  Report success or failure
