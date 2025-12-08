removeInstall() {
    sudo apt remove -y firefox-esr evolution yelp gnome-contacts gnome-weather gnome-clocks gnome-maps libreoffice-calc libreoffice-draw libreoffice-impress libreoffice-writer shotwell simple-scan gnome-tour seahorse gnome-connections malcontent-gui libreoffice-common gnome-calculator
}

loadSetting() {
    dconf load / < gnome-settings-backup.ini
}

pre_installTreeCurlFlatpakVmAnki() {
    sudo apt install -y tree curl flatpak gnome-software-plugin-flatpak qemu-system qemu-kvm libvirt-daemon-system libvirt-clients virt-manager libxcb-xinerama0 libxcb-cursor0 libnss3
}

braveInstall() {
    sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && sudo curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources
}

ankiInstall() {
    tar --use-compress-program=unzstd -xf anki-launcher-25.09-linux.tar.zst && cd anki-launcher-25.09-linux && sudo ./install.sh && cd - > /dev/null
}

codiumInstall() {
    wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg && echo -e 'Types: deb\nURIs: https://download.vscodium.com/debs\nSuites: vscodium\nComponents: main\nArchitectures: amd64 arm64\nSigned-by: /usr/share/keyrings/vscodium-archive-keyring.gpg' | sudo tee /etc/apt/sources.list.d/vscodium.sources
}

vpnDownload() {
    wget https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.8_all.deb
}

syncInstall() {
    sudo mkdir -p /etc/apt/keyrings && sudo curl -L -o /etc/apt/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg && echo "deb [signed-by=/etc/apt/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable-v2" | sudo tee /etc/apt/sources.list.d/syncthing.list
}

grubFix() {
    sudo sed -i 's/^#GRUB_TERMINAL=console/GRUB_TERMINAL=console/' /etc/default/grub || echo 'GRUB_TERMINAL=console' | sudo tee -a /etc/default/grub >/dev/null && sudo update-grub
}

screenshotLink() {
    rm -r /home/ahdimsun/Pictures/Screenshots
ln -s /home/ahdimsun/Danish/Screenshots /home/ahdimsun/Pictures/Screenshots
}

flatpkInstall() {
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
}

flatpkInstallInstall() {
    flatpak install -y flathub org.kde.kdenlive
}

vmInstall() {
    sudo usermod -aG libvirt,kvm $(whoami) && sudo systemctl enable --now libvirtd
}

post_installBraveVpnSync() {
    sudo apt install -y brave-browser codium proton-vpn-gnome-desktop syncthing
}

removeFileFolder() {
    rm -f ./protonvpn-stable-release_1.0.8_all.deb
rm -rf ./anki-launcher-25.09-linux
}

sudo apt install ./obsidian_1.9.14_amd64.deb
sudo apt install ./protonvpn-stable-release_1.0.8_all.deb

sudo dpkg --add-architecture i386
sudo apt update

sudo apt-get install libc6:i386 libncurses6:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386

sudo apt install fonts-noto

sudo virsh net-start default

sudo virsh net-autostart default





















# title for gnome terminal
set_title() {
    echo -ne "\033]0;$1\007"
}

# remove pre installed gnome stuff on fresh install
remove_preinstall() {
    sudo apt remove -y gnome-contacts gnome-weather gnome-clocks gnome-maps gnome-calendar gnome-music simple-scan gnome-snapshot gnome-characters seahorse gnome-connections gnome-disk-utility baobab gnome-system-monitor gnome-logs malcontent-gui totem gnome-sound-recorder gnome-tour shotwell libreoffice-calc libreoffice-draw libreoffice-impress libreoffice-writer libreoffice-common gnome-text-editor yelp firefox-esr evolution
}

















sudo apt update && sudo apt upgrade -y && sudo apt update

clear

remove_preinstall

sudo apt autoremove -y && sudo apt update && sudo apt upgrade -y && sudo apt update

clear