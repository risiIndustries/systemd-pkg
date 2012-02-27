Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Version:        26
Release:        17%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Summary:        A System and Service Manager
BuildRequires:  libudev-devel >= 160
BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-libs-devel
BuildRequires:  cryptsetup-luks-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  vala >= 0.11
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  libnotify-devel >= 0.7
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
Requires(post): authconfig
Requires:       systemd-units = %{version}-%{release}
Requires:       dbus >= 1.4.6-3.fc15
Requires:       udev >= 167
Requires:       libudev >= 160
Requires:       initscripts >= 9.28
Requires:       filesystem >= 2.4.40
Conflicts:      selinux-policy < 3.9.16-12.fc15
Requires:       kernel >= 2.6.35.2-9.fc14
Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.bz2
# Adds support for the %%{_unitdir} macro
Source1:        macros.systemd
Source2:        systemd-sysv-convert
Patch0:         0001-dbus-common-fix-segfault-when-a-DBus-message-has-no-.patch
Patch1:         0001-readahead-collect-ignore-EACCES-for-fanotify.patch
Patch2:         0001-vconsole-use-open_terminal-instead-of-open.patch
Patch3:         0001-pam-downgrade-a-few-log-msgs.patch
Patch4:         0001-systemctl-fix-double-unref-of-a-dbus-message.patch
Patch5:         0001-cryptsetup-generator-fix-etc-cryptsetup-options.patch
Patch6:         0001-readahead-common-fix-total-memory-size-detection.patch
Patch7:         0001-systemctl-fix-is-enabled-for-native-units-under-lib.patch
Patch8:         0001-dbus-fix-name-of-capability-property.patch
Patch9:         0001-pam-module-add-debug-parameter.patch
Patch10:        0001-systemctl-Add-SYSTEMD_PAGER-for-setting-the-pager-to.patch
Patch11:        0001-manager-include-full-systemctl-status-command-line-i.patch
Patch12:        0001-swap-ignore-missing-proc-swaps.patch
Patch13:        0001-unit-when-loading-symlinked-template-units-properly-.patch
Patch14:        0001-execute-don-t-choke-when-systemd-was-compiled-with-a.patch
Patch15:        0001-execute-fix-PAM-error-checking.patch
Patch16:        0001-umount-ignore-missing-proc-swaps.patch
Patch17:        0001-units-enable-dev-hugepages.automount-and-dev-mqueue..patch
Patch18:        0001-tmpfiles-don-t-exit-with-an-error-code-if-we-cannot-.patch
Patch19:        0001-manager-consider-the-active-job-when-merging.patch
Patch20:        0001-shutdown-accept-minutes-argument-without.patch
Patch21:        0001-shutdown-respect-the-dry-run-option-k.patch
Patch22:        0001-shutdown-print-the-standard-wall-message-even-when-t.patch
Patch23:        0001-systemadm-report-GLib.Error-only-to-stderr.patch
Patch24:        0001-password-agent-make-sure-not-to-access-unallocated-m.patch
Patch25:        0001-password-agent-actually-really-don-t-access-unalloca.patch
# Cannot apply this yet because of bz719931
#Patch26:        0001-service-pidfile-in-SysV-chkconfig-header-implies-a-r.patch
Patch27:        0001-cgroup-don-t-trim-a-cgroup-we-create-we-might-just-t.patch
Patch28:        0001-manager-merge-serialization-and-desrialization-count.patch
Patch29:        0001-execute-properly-enforce-group.patch
Patch30:        0001-manager-call-generators-with-umask-0022.patch
Patch31:        0001-getty-automatically-spawn-getty-on-xen-console-xvc0.patch
Patch32:        0001-manager-add-log-control-via-RT-signals.patch
Patch33:        0001-Don-t-show-a-warning-message-in-non-enforcing-mode.patch
Patch34:        0001-strv-fix-counting-in-strv_env_delete.patch
Patch35:        0001-tmpfiles-Remove-X11-lock-files-for-displays-10-and-h.patch
Patch36:        0001-cryptsetup-accept-none-option.patch
# May cause a new dep cycle, related to bz711150
#Patch37:        0001-cryptsetup-generator-block-boot-when-querying-passph.patch
Patch38:        0001-execute-fix-bus-serialization-for-commands.patch
Patch39:        0001-specifier-drop-misplaced-assert.patch
Patch40:        0001-getty-generator-ignore-if-symlinks-already-exist.patch
Patch41:        0001-mount-fix-parsing-of-prio-value.patch
Patch42:        0001-systemctl-if-we-managed-to-reexec-the-init-system-vi.patch
Patch43:        0001-dropin-don-t-fail-if-random-files-are-stored-in-.wan.patch
Patch44:        0001-getty-automatically-add-getty-on-hvsi0-virtualizer-c.patch
Patch45:        0001-getty-simplify-things-a-bit.patch
Patch46:        0001-locale-support-LANGUAGE-too.patch
Patch47:        0001-fsck-show-progress-while-fscking-at-boot.patch
Patch48:        0001-stdout-bridge-set-facility-of-messages-with-no-facil.patch
Patch49:        0001-condition-opt-out-of-proc-cmdline-parsing-only-when-.patch
Patch50:        0001-stdout-syslog-bridge-properly-handle-overly-long-log.patch
Patch51:        0001-units-direct-stdout-stderr-of-rescue-shells-to-tty.patch
Patch52:        0001-service-handle-forking-services-that-move-to-a-new-P.patch
Patch53:        0001-service-minor-change-in-service_load_pid_file-return.patch
Patch54:        0001-modules-load-filter-out-double-modules.patch
Patch55:        0001-job-after-converting-a-job-from-restart-to-start-rea.patch
Patch56:        0001-mount-pull-in-quota-tools-from-fstab-lines-with-quot.patch
Patch57:        0001-service-if-StandardInput-socket-and-StandardOutput-i.patch
Patch58:        0001-unit-don-t-recheck-conditions-when-a-unit-is-already.patch
Patch59:        0001-units-fix-rescue.service-race-with-plymouth.patch
Patch60:        0001-coverity-fix-a-couple-of-bugs-found-by-coverity.patch
Patch61:        0001-condition-fix-reversed-tests-if-path-does-not-exist-.patch
Patch62:        0001-manager-fix-job-mode-for-SIGRTMIN-1-2.patch
Patch63:        0001-llvm-analyze-fix-some-bugs-found-by-llvm-analyze.patch
# May be risky. See what it caused in F16 in bz741078.
#Patch64:        0001-unit-fix-complementing-of-requirement-deps-with-Afte.patch
Patch65:        0001-service-fix-up-std-output-error-before-we-add-depend.patch
Patch66:        0001-test_virtualization-do-not-try-to-compare-id-in-virt.patch
Patch67:        0001-tmpfiles-fix-file-descriptor-leak.patch
Patch68:        0001-util-fix-close-call-on-wrong-variable.patch
Patch69:        0001-readahead-lower-max-file-size-for-readahead.patch
Patch70:        0001-units-introduce-local-fs-pre.target-and-remote-fs-pr.patch
Patch71:        0001-units-forgot-target-units.patch
Patch72:        0001-units-remount-root-and-API-FS-before-all-mount-units.patch
Patch73:        0001-service-don-t-try-to-guess-PID-for-SysV-services-any.patch
Patch74:        0002-manager-fix-a-crash-in-isolating.patch
Patch75:        0001-mount-order-remote-mounts-after-both-network.target-.patch
Patch76:        0001-units-drop-Install-section-from-remote-fs-pre.target.patch
Patch77:        0001-unit-fix-false-positive-in-check-for-unneeded-unit.patch
Patch78:        0002-unit-check-for-unneeded-dependencies-even-when-unit-.patch
Patch79:        0001-utmp-remove-unneded-parameters.patch
Patch80:        0002-utmp-no-need-to-zero-a-struct-before-overwriting-it-.patch
Patch81:        0003-utmp-initialize-store-with-the-found-entry-not-with-.patch
Patch82:        0004-utmp-for-DEAD_PROCESS-write-the-current-time-to-wtmp.patch
Patch83:        0001-unit-garbage-collect-units-with-load-error.patch
Patch84:        0001-mount-fix-quota.patch
Patch85:        0001-mount-fix-automount-regression.patch
Patch86:        0001-socket-add-option-for-SO_PASSCRED.patch
Patch87:        0002-shutdownd-use-PassCred-yes-in-the-socket-unit.patch
Patch88:        0003-syslog-use-PassCred-yes-for-the-dev-log-socket.patch
Patch89:        0004-man-document-the-PassCred-option.patch
Patch90:        0001-socket-rename-the-PassCred-option-to-PassCredentials.patch
Patch91:        util-add-parse_uid.patch
Patch92:        0001-shutdown-exclude-processes-with-argv-0-0-from-killin.patch

Patch100:       fedora-storage-detect-encrypted-PVs.patch

# For sysvinit tools
Obsoletes:      SysVinit < 2.86-24, sysvinit < 2.86-24
Provides:       SysVinit = 2.86-24, sysvinit = 2.86-24
Provides:       sysvinit-userspace
Provides:       systemd-sysvinit
Obsoletes:      systemd-sysvinit
Obsoletes:      upstart < 1.2-3
Obsoletes:      upstart-sysvinit < 1.2-3
Conflicts:      upstart-sysvinit
Obsoletes:      readahead < 1:1.5.7-3
Provides:       readahead = 1:1.5.7-3

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package units
Group:          System Environment/Base
Summary:        Configuration files, directories and installation tool for systemd
Requires:       pkgconfig
Requires(post): coreutils
Requires(post): gawk

%description units
Basic configuration files, directories and installation tool for the systemd
system and service manager.

%package gtk
Group:          System Environment/Base
Summary:        Graphical frontend for systemd
Requires:       %{name} = %{version}-%{release}
Requires:       polkit

%description gtk
Graphical front-end for systemd.

%package sysv
Group:          System Environment/Base
Summary:        SysV tools for systemd
Requires:       %{name} = %{version}-%{release}

%description sysv
SysV compatibility tools for systemd

%prep
%setup -q
set +x
for p in %{patches}; do
        echo "Applying $p"
        patch -p1 < $p
done
set -x

%build
%configure --with-rootdir= --with-distro=fedora
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}/sbin
ln -s ../bin/systemd %{buildroot}/sbin/init
ln -s ../bin/systemctl %{buildroot}/sbin/reboot
ln -s ../bin/systemctl %{buildroot}/sbin/halt
ln -s ../bin/systemctl %{buildroot}/sbin/poweroff
ln -s ../bin/systemctl %{buildroot}/sbin/shutdown
ln -s ../bin/systemctl %{buildroot}/sbin/telinit
ln -s ../bin/systemctl %{buildroot}/sbin/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}/etc/systemd/system/*.target.wants

# Make sure the ghost-ing below works
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel2.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel3.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel4.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %{buildroot}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}/lib/systemd/system/syslog.target.wants

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/os-release
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info

# Install RPM macros file for systemd
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/

# Install SysV conversion tool for systemd
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/systemd-machine-id-setup > /dev/null 2>&1 || :
/bin/systemctl daemon-reexec > /dev/null 2>&1 || :

# Make sure pam_systemd is enabled
if ! /bin/grep -q pam_systemd /etc/pam.d/system-auth-ac ; then
        /usr/sbin/authconfig --update >/dev/null 2>&1 || :

        # Try harder
        /bin/grep -q pam_systemd /etc/pam.d/system-auth-ac || /usr/sbin/authconfig --updateall >/dev/null 2>&1 || :
fi

%post units
if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(/bin/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="/lib/systemd/system/graphical.target"
        else
                target="/lib/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        /bin/ln -sf "$target" /etc/systemd/system/default.target > /dev/null 2>&1 || :

        # Enable the services we install by default.
        /bin/systemctl enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                hwclock-load.service > /dev/null 2>&1 || :
fi

%preun units
if [ $1 -eq 0 ] ; then
        /bin/systemctl disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                hwclock-load.service > /dev/null 2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target > /dev/null 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload > /dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%dir %{_sysconfdir}/systemd/user
%{_sysconfdir}/xdg/systemd
%{_libdir}/../lib/tmpfiles.d/systemd.conf
%{_libdir}/../lib/tmpfiles.d/x11.conf
%{_libdir}/../lib/tmpfiles.d/legacy.conf
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/os-release
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
/bin/systemd
/bin/systemd-notify
/bin/systemd-ask-password
/bin/systemd-tty-ask-password-agent
/bin/systemd-machine-id-setup
/usr/bin/systemd-nspawn
/usr/bin/systemd-stdio-bridge
/usr/bin/systemd-analyze
/lib/systemd/systemd-*
/lib/udev/rules.d/*.rules
%dir /lib/systemd/system-generators
%dir /lib/systemd/system-shutdown
/lib/systemd/system-generators/systemd-cryptsetup-generator
/lib/systemd/system-generators/systemd-getty-generator
/%{_lib}/security/pam_systemd.so
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%{_bindir}/systemd-cgls
%{_mandir}/man1/*
%exclude %{_mandir}/man1/systemctl.*
%exclude %{_mandir}/man1/systemadm.*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_libdir}/../lib/systemd
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_docdir}/systemd
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy

%files units
%defattr(-,root,root,-)
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/bash_completion.d
%dir /lib/systemd
%dir %{_libdir}/../lib/tmpfiles.d
%dir %{_libdir}/../lib/sysctl.d
%dir %{_libdir}/../lib/modules-load.d
%dir %{_libdir}/../lib/binfmt.d
/lib/systemd/system
/bin/systemctl
/bin/systemd-tmpfiles
%{_sysconfdir}/bash_completion.d/systemctl-bash-completion.sh
%{_sysconfdir}/rpm/macros.systemd
%{_mandir}/man1/systemctl.*
%{_datadir}/pkgconfig/systemd.pc
%{_docdir}/systemd/LICENSE

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files gtk
%defattr(-,root,root,-)
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.*

%files sysv
%{_bindir}/systemd-sysv-convert

%changelog
* Mon Feb 27 2012 Michal Schmidt <mschmidt@redhat.com> - 26-17
- Backport the detection of root storage daemons.
  http://www.freedesktop.org/wiki/Software/systemd/RootStorageDaemons

* Tue Jan 31 2012 Michal Schmidt <mschmidt@redhat.com> - 26-16
- Backport PassCredentials to avoid #757628 when F15 kernel is rebased to 3.2.

* Tue Jan 31 2012 Michal Schmidt <mschmidt@redhat.com> - 26-15
- Fix quota (#773431).

* Tue Jan 17 2012 Michal Schmidt <mschmidt@redhat.com> - 26-14
- Slowing down in F15. Only a few fixes for bugs reported against F15:
  - StopWhenUnneeded
  - wtmp
  - gc of units with load error

* Wed Nov 02 2011 Michal Schmidt <mschmidt@redhat.com> - 26-13
- Fix remote-fs-pre.target and its ordering.
- Fixes: BZ#749940

* Wed Oct 19 2011 Michal Schmidt <mschmidt@redhat.com> - 26-12
- Fix a crash in isolating.
- Fixes: BZ#717325

* Wed Oct 12 2011 Michal Schmidt <mschmidt@redhat.com> - 26-11
- Pick a few fixes from upstream v37.
- Including the change to disable main PID guessing for SysV services.
- Loop over %%{patches} in the spec.
- Fixes: BZ#718464, fdo#41336

* Sun Sep 25 2011 Michal Schmidt <mschmidt@redhat.com> - 26-10
- Pick lots of fixes from upstream up to v36.
- A few features added too:
  - support more types of virtual serial consoles in getty-generator
  - log control via RT signals
  - support for LANGUAGE in environment
  - show fsck progress on the console
- Fixes: BZ#735013, BZ#722803, BZ#736360, BZ#698198, BZ#710487
- Fixes: fdo39957, fdo39818, fdo40510

* Tue Aug 23 2011 Lennart Poettering <lpoetter@redhat.com> - 26-9
- Fix a couple of bugs (#723892, #726976)

* Fri Jul 08 2011 Michal Schmidt <mschmidt@redhat.com> - 26-8
- Drop the pidfile patch for now. It exposes a bug in sendmail (BZ#719884)

* Wed Jul 06 2011 Michal Schmidt <mschmidt@redhat.com> - 26-7
- Add more fixes from upstream:
  - don't trim cgroups on reexec (BZ#678555)
  - treat SysV services with "pidfile:" header as real daemons (BZ#702621)

* Mon Jul 04 2011 Michal Schmidt <mschmidt@redhat.com> - 26-6
- Cherry-picked a bunch of upstream patches.
- Fixes: BZ#633774, BZ#708886, BZ#712710, BZ#716663
- Partially fixes: BZ#624149
- other small fixes

* Mon Jun 20 2011 Michal Schmidt <mschmidt@redhat.com> - 26-5
- Temporary workaround to detect LVM VGs on encrypted PVs. (BZ#708684)

* Wed Jun 15 2011 Michal Schmidt <mschmidt@redhat.com> - 26-4
- Pick bugfixes from upstream:
- systemctl: fix 'is-enabled' for native units under /lib (BZ#699027)
- dbus: fix name of capability property
- pam-module: add debug= parameter (BZ#705427)

* Sun Jun 12 2011 Michal Schmidt <mschmidt@redhat.com> - 26-3
- Pick bugfixes from upstream:
- systemctl: fix double unref of a dbus message (BZ#709909)
- cryptsetup-generator: fix /etc/cryptsetup options (BZ#710839)
- readahead-common: fix total memory size detection (BZ#712341)

* Wed May 25 2011 Lennart Poettering <lpoetter@redhat.com> - 26-2
- Bugfix release
- https://bugzilla.redhat.com/show_bug.cgi?id=707507
- https://bugzilla.redhat.com/show_bug.cgi?id=707483
- https://bugzilla.redhat.com/show_bug.cgi?id=705427
- https://bugzilla.redhat.com/show_bug.cgi?id=707577

* Sat Apr 30 2011 Lennart Poettering <lpoetter@redhat.com> - 26-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=699394
- https://bugzilla.redhat.com/show_bug.cgi?id=698198
- https://bugzilla.redhat.com/show_bug.cgi?id=698674
- https://bugzilla.redhat.com/show_bug.cgi?id=699114
- https://bugzilla.redhat.com/show_bug.cgi?id=699128

* Thu Apr 21 2011 Lennart Poettering <lpoetter@redhat.com> - 25-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694788
- https://bugzilla.redhat.com/show_bug.cgi?id=694321
- https://bugzilla.redhat.com/show_bug.cgi?id=690253
- https://bugzilla.redhat.com/show_bug.cgi?id=688661
- https://bugzilla.redhat.com/show_bug.cgi?id=682662
- https://bugzilla.redhat.com/show_bug.cgi?id=678555
- https://bugzilla.redhat.com/show_bug.cgi?id=628004

* Wed Apr  6 2011 Lennart Poettering <lpoetter@redhat.com> - 24-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694079
- https://bugzilla.redhat.com/show_bug.cgi?id=693289
- https://bugzilla.redhat.com/show_bug.cgi?id=693274
- https://bugzilla.redhat.com/show_bug.cgi?id=693161

* Tue Apr  5 2011 Lennart Poettering <lpoetter@redhat.com> - 23-1
- New upstream release
- Include systemd-sysv-convert

* Fri Apr  1 2011 Lennart Poettering <lpoetter@redhat.com> - 22-1
- New upstream release

* Wed Mar 30 2011 Lennart Poettering <lpoetter@redhat.com> - 21-2
- The quota services are now pulled in by mount points, hence no need to enable them explicitly

* Tue Mar 29 2011 Lennart Poettering <lpoetter@redhat.com> - 21-1
- New upstream release

* Mon Mar 28 2011 Matthias Clasen <mclasen@redhat.com> - 20-2
- Apply upstream patch to not send untranslated messages to plymouth

* Tue Mar  8 2011 Lennart Poettering <lpoetter@redhat.com> - 20-1
- New upstream release

* Tue Mar  1 2011 Lennart Poettering <lpoetter@redhat.com> - 19-1
- New upstream release

* Wed Feb 16 2011 Lennart Poettering <lpoetter@redhat.com> - 18-1
- New upstream release

* Mon Feb 14 2011 Bill Nottingham <notting@redhat.com> - 17-6
- bump upstart obsoletes (#676815)

* Wed Feb  9 2011 Tom Callaway <spot@fedoraproject.org> - 17-5
- add macros.systemd file for %%{_unitdir}

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Lennart Poettering <lpoetter@redhat.com> - 17-3
- Fix popen() of systemctl, #674916

* Mon Feb  7 2011 Bill Nottingham <notting@redhat.com> - 17-2
- add epoch to readahead obsolete

* Sat Jan 22 2011 Lennart Poettering <lpoetter@redhat.com> - 17-1
- New upstream release

* Tue Jan 18 2011 Lennart Poettering <lpoetter@redhat.com> - 16-2
- Drop console.conf again, since it is not shipped in pamtmp.conf

* Sat Jan  8 2011 Lennart Poettering <lpoetter@redhat.com> - 16-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 15-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 14-1
- Upstream update
- Enable hwclock-load by default
- Obsolete readahead
- Enable /var/run and /var/lock on tmpfs

* Fri Nov 19 2010 Lennart Poettering <lpoetter@redhat.com> - 13-1
- new upstream release

* Wed Nov 17 2010 Bill Nottingham <notting@redhat.com> 12-3
- Fix clash

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-2
- Don't clash with initscripts for now, so that we don't break the builders

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-1
- New upstream release

* Fri Nov 12 2010 Matthias Clasen <mclasen@redhat.com> - 11-2
- Rebuild with newer vala, libnotify

* Thu Oct  7 2010 Lennart Poettering <lpoetter@redhat.com> - 11-1
- New upstream release

* Wed Sep 29 2010 Jesse Keating <jkeating@redhat.com> - 10-6
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Bill Nottingham <notting@redhat.com> - 10-5
- merge -sysvinit into main package

* Mon Sep 20 2010 Bill Nottingham <notting@redhat.com> - 10-4
- obsolete upstart-sysvinit too

* Fri Sep 17 2010 Bill Nottingham <notting@redhat.com> - 10-3
- Drop upstart requires

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-2
- Enable audit
- https://bugzilla.redhat.com/show_bug.cgi?id=633771

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=630401
- https://bugzilla.redhat.com/show_bug.cgi?id=630225
- https://bugzilla.redhat.com/show_bug.cgi?id=626966
- https://bugzilla.redhat.com/show_bug.cgi?id=623456

* Fri Sep  3 2010 Bill Nottingham <notting@redhat.com> - 9-3
- move fedora-specific units to initscripts; require newer version thereof

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-2
- Add missing tarball

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-1
- New upstream version
- Closes 501720, 614619, 621290, 626443, 626477, 627014, 627785, 628913

* Fri Aug 27 2010 Lennart Poettering <lpoetter@redhat.com> - 8-3
- Reexecute after installation, take ownership of /var/run/user
- https://bugzilla.redhat.com/show_bug.cgi?id=627457
- https://bugzilla.redhat.com/show_bug.cgi?id=627634

* Thu Aug 26 2010 Lennart Poettering <lpoetter@redhat.com> - 8-2
- Properly create default.target link

* Wed Aug 25 2010 Lennart Poettering <lpoetter@redhat.com> - 8-1
- New upstream release

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623561

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-2
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623430

* Tue Aug 10 2010 Lennart Poettering <lpoetter@redhat.com> - 7-1
- New upstream release

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-2
- properly hide output on package installation
- pull in coreutils during package installtion

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-1
- New upstream release
- Fixes #621200

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-2
- Add tarball

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-1
- Prepare release 5

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 4-4
- Add 'sysvinit-userspace' provide to -sysvinit package to fix upgrade/install (#618537)

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-3
- Add libselinux to build dependencies

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-2
- Use the right tarball

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-1
- New upstream release, and make default

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-3
- Used wrong tarball

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-2
- Own /cgroup jointly with libcgroup, since we don't dpend on it anymore

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-1
- New upstream release

* Fri Jul 9 2010 Lennart Poettering <lpoetter@redhat.com> - 2-0
- New upstream release

* Wed Jul 7 2010 Lennart Poettering <lpoetter@redhat.com> - 1-0
- First upstream release

* Tue Jun 29 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.7.20100629git4176e5
- New snapshot
- Split off -units package where other packages can depend on without pulling in the whole of systemd

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.6.20100622gita3723b
- Add missing libtool dependency.

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.5.20100622gita3723b
- Update snapshot

* Mon Jun 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.4.20100614git393024
- Pull the latest snapshot that fixes a segfault. Resolves rhbz#603231

* Thu Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
