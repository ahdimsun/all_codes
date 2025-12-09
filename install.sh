#!/usr/bin/env bash

fix_grub() {
    sudo sed -i 's/^#GRUB_TERMINAL=console/GRUB_TERMINAL=console/' /etc/default/grub || echo 'GRUB_TERMINAL=console' | sudo tee -a /etc/default/grub >/dev/null && sudo update-grub
}

symlink_screenshot_folder() {
    [ -d "/home/ahdimsun/Pictures/Screenshots" ] && rm -r "/home/ahdimsun/Pictures/Screenshots"; ln -s "/home/ahdimsun/Danish/Screenshots" "/home/ahdimsun/Pictures/Screenshots"
}

install_anki() {
    tarball=$(ls -t anki*.tar.zst | head -n1) && folder="${tarball%.tar.zst}" && tar --use-compress-program=unzstd -xf "$tarball" && cd "$folder" && sudo ./install.sh && cd -
}

install_preinstall() {
    sudo apt install -y tree curl virt-manager libxcb-xinerama0 libxcb-cursor0 libnss3 flatpak gnome-software-plugin-flatpak libc6:i386 libncurses6:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386 git vlc
}

enable_virt_manager() {
    sudo usermod -aG libvirt,kvm "$USER" && sudo systemctl enable --now libvirtd && sudo virsh net-start default && sudo virsh net-autostart default
}

install_brave() {
    sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg && sudo curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources
}

install_codium() {
    wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg && echo -e 'Types: deb\nURIs: https://download.vscodium.com/debs\nSuites: vscodium\nComponents: main\nArchitectures: amd64 arm64\nSigned-by: /usr/share/keyrings/vscodium-archive-keyring.gpg' | sudo tee /etc/apt/sources.list.d/vscodium.sources
}

install_sync() {
    sudo mkdir -p /etc/apt/keyrings && sudo curl -L -o /etc/apt/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg && echo "deb [signed-by=/etc/apt/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable-v2" | sudo tee /etc/apt/sources.list.d/syncthing.list
}

install_flathub() {
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
}

install_vpn() {
    wget https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.8_all.deb
}

install_debinstall() {
    sudo apt install ./*.deb -y
}

install_flathub_app() {
    flatpak install -y flathub org.kde.kdenlive
}

install_postinstall() {
    sudo apt install -y brave-browser codium proton-vpn-gnome-desktop syncthing
}

remove_preinstall() {
    sudo apt remove -y gnome-contacts gnome-weather gnome-clocks gnome-maps gnome-calendar gnome-music simple-scan gnome-snapshot gnome-characters seahorse gnome-connections gnome-disk-utility baobab gnome-system-monitor gnome-logs malcontent-gui totem gnome-sound-recorder gnome-tour shotwell libreoffice-calc libreoffice-draw libreoffice-impress libreoffice-writer libreoffice-common gnome-text-editor yelp firefox-esr evolution gnome-calculator
}

load_setting_gnome() {
    dconf load / < gnome-settings-backup.ini
}

set_git_github() {
    git config --global user.name "Muhammad Danish" && git config --global user.email "ahdimsun@gmail.com" && ssh-keygen -t ed25519 -C "ahdimsun@gmail.com" -f ~/.ssh/id_ed25519 -N "" && ssh-add ~/.ssh/id_ed25519 && cat ~/.ssh/id_ed25519.pub > key.txt
}

install_android_studio() {
    sudo mv android-studio /usr/local/ && cd /usr/local/android-studio/bin && sudo ./studio.sh
}
# && eval "$(ssh-agent -s)"

sudo dpkg --add-architecture i386

sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y

fix_grub

symlink_screenshot_folder

install_anki

install_preinstall

set_git_github

enable_virt_manager

install_brave

install_codium

install_sync

install_flathub

install_vpn

install_debinstall

sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y

install_postinstall

install_flathub_app

remove_preinstall

sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y

install_android_studio

load_setting_gnome