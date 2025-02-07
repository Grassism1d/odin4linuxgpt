# Maintainer: Your Name <luvurselfidk@gmail.com>
pkgname=odin-flasher
pkgver=1.0.0
pkgrel=1
pkgdesc="A Odin/ADB tools app that was ENTIRELY made by chatgpt. "
arch=('x86_64')
url="https://github.com/Grassism1d/odin4linuxgpt/tree/main"
license=('GPL3')
depends=('python' 'tk' 'heimdall')
source=("$pkgname.py" "odin_flasher.desktop" "odin_flasher.png")
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
    install -Dm755 "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "odin_flasher.desktop" "$pkgdir/usr/share/applications/odin_flasher.desktop"
    install -Dm644 "odin_flasher.png" "$pkgdir/usr/share/pixmaps/odin_flasher.png"
}
