import difflib


software = ['wget', 'tzdata', 'trousers', 'teamd', 'teamd', 'tar', 'systemd-sysv',
            'systemd-sysv', 'sudo', 'snappy', 'rpm-python27', 'rpm-build-libs', 'rootfiles',
            'rdma', 'quota', 'pyxattr', 'python27-virtualenv', 'python27-simplejson', 'python-iniparse',
            'python-IPy', 'python', 'pygpgme', 'pygobject3-base', 'procmail', 'pm-utils', 'pinentry',
            'perl-threads', 'perl-libs', 'parted', 'os-prober', 'openssh-clients', 'oci-register-machine',
            'nss-softokn-freebl', 'nss-softokn-freebl', 'npm', 'net-tools', 'mesa-libGL', 'mariadb-libs',
            'lua', 'libuser', 'libselinux-utils', 'libproxy', 'libpipeline', 'libpciaccess', 'libpciaccess',
            'libpath_utils', 'libnl3', 'libini_config', 'libidn', 'libgssglue', 'libgomp', 'libgcrypt', 'libgcrypt',
            'libgcc', 'libedit', 'libdb', 'libcom_err', 'libcom_err', 'libcap-ng', 'libXfixes', 'libSM',
            'kernel-headers', 'kbd', 'java-1.8.0-openjdk', 'initscripts', 'hardlink', 'hardlink', 'hardlink',
            'gssproxy', 'groff-base', 'grep', 'gobject-introspection', 'freetype', 'fipscheck', 'ethtool',
            'elfutils-libelf', 'diffutils', 'device-mapper-event', 'device-mapper-event', 'dejavu-sans-fonts',
            'curl', 'crontabs', 'cronie', 'container-selinux', 'container-selinux', 'chkconfig', 'chkconfig',
            'checkpolicy', 'bzip2', 'bind-license', 'aws-cfn-bootstrap', 'aws-cfn-bootstrap', 'aws-cfn-bootstrap',
            'audit-libs', 'NetworkManager-team', 'Amazon SSM Agent', 'Amazon SSM Agent', 'AWS Tools for Windows',
            'httpd']

def calculate(input_string):
    match_result = {}

    for software_name in software:
        match_result[software_name] = difflib.SequenceMatcher(None, software_name, input_string).ratio()
        print(difflib.SequenceMatcher(None, software_name, input_string).ratio())

    for k, v in sorted(match_result.items(), key=lambda x: x[1]):
        print(str(k) + ": " + str(v))

if __name__ == '__main__':
    product = 'http_server'
    calculate(product)
