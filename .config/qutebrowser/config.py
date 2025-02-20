config.load_autoconfig(False)
c.colors.completion.category.bg = "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #232429)"
c.colors.completion.category.border.bottom = "#3f4147"
c.colors.completion.category.border.top = "#3f4147"
c.colors.completion.category.fg = "#e1acff"
c.colors.completion.even.bg = "#232429"
c.colors.completion.fg = ["#9cc4ff", "white", "white"]
c.colors.completion.item.selected.bg = "#74418a"
c.colors.completion.item.selected.border.bottom = "#74418a"
c.colors.completion.item.selected.border.top = "#74418a"
c.colors.completion.item.selected.fg = "#000000"
c.colors.completion.item.selected.match.fg = "#c678dd"
c.colors.completion.match.fg = "#c678dd"
c.colors.completion.odd.bg = "#1c1f24"
c.colors.completion.scrollbar.fg = "white"
c.colors.contextmenu.disabled.fg = "#666666"
c.colors.contextmenu.menu.bg = "#111111"
c.colors.contextmenu.menu.fg = "#FFFFFF"
c.colors.contextmenu.selected.bg = "#0080FF"
c.colors.contextmenu.selected.fg = "#FFFFFF"
c.colors.downloads.bar.bg = "#282c34"
c.colors.downloads.error.bg = "#ff6c6b"
c.colors.hints.fg = "#282c34"
c.colors.hints.match.fg = "#98be65"
c.colors.messages.info.bg = "#282c34"
c.colors.statusbar.command.bg = "#282c34"
c.colors.statusbar.insert.bg = "#497920"
c.colors.statusbar.insert.fg = "white"
c.colors.statusbar.normal.bg = "#282c34"
c.colors.statusbar.passthrough.bg = "#34426f"
c.colors.statusbar.url.warn.fg = "yellow"
c.colors.tabs.bar.bg = "#1c1f34"
c.colors.tabs.even.bg = "#282c34"
c.colors.tabs.odd.bg = "#282c34"
c.colors.tabs.pinned.even.bg = "darkseagreen"
c.colors.tabs.pinned.odd.bg = "seagreen"
c.colors.tabs.pinned.selected.even.bg = "#282c34"
c.colors.tabs.pinned.selected.odd.bg = "#282c34"
c.colors.tabs.selected.even.bg = "#282c34"
c.colors.tabs.selected.odd.bg = "#282c34"
c.colors.webpage.bg = "#000000"
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.enabled = True
c.completion.cmd_history_max_items = 100
c.completion.height = "30%"
c.completion.open_categories = ["quickmarks", "history"]
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 0
c.completion.show = "always"
c.completion.shrink = True
c.completion.timestamp_format = ""
c.completion.web_history.max_items = 7
c.content.autoplay = False
c.content.blocking.adblock.lists = ["https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2024.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt", "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/thirdparties/pgl.yoyo.org/as/serverlist", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts", "https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt", "https://fanboy.co.nz/fanboy-problematic-sites.txt", "https://easylist.to/easylist/easylist.txt", "https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt", "https://raw.github.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt", "https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt", "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt", "https://easylist-msie.adblockplus.org/abp-filters-anti-cv.txt", "https://raw.githubusercontent.com/abp-filters/abp-filters-anti-cv/master/english.txt", "https://raw.githubusercontent.com/k2jp/abp-japanese-filters/master/abpjf.txt", "https://www.joinhoney.com/whitelist/honey-smart-shopping.txt"]
c.content.blocking.enabled = True
c.content.blocking.hosts.lists = ["https://raw.githubusercontent.com/mmotti/pihole-regex/master/regex.list", "https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Extension/GoodbyeAds-YouTube-AdBlock.txt", "http://someonewhocares.org/hosts/hosts", "http://winhelp2002.mvps.org/hosts.zip", "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext", "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"]
c.content.blocking.method = "both"
c.content.cache.maximum_pages = 500
c.content.cookies.accept = "no-unknown-3rdparty"
c.content.dns_prefetch = True
c.content.headers.do_not_track = True
c.content.javascript.enabled = False
c.content.media.audio_capture = False
c.content.media.audio_video_capture = False
c.content.pdfjs = True
c.content.user_stylesheets = ["~/.config/qutebrowser/schemes/minimal.css"]
c.content.webgl = True
c.downloads.location.directory = "/home/sorath/Transferências"
c.downloads.remove_finished = 0
c.scrolling.bar = "never"
c.scrolling.smooth = True
c.tabs.show = "multiple"
config.bind("<Ctrl-0>", "tab-focus 10", mode="command")
config.bind("<Ctrl-1>", "tab-focus 1", mode="command")
config.bind("<Ctrl-2>", "tab-focus 2", mode="command")
config.bind("<Ctrl-3>", "tab-focus 3", mode="command")
config.bind("<Ctrl-4>", "tab-focus 4", mode="command")
config.bind("<Ctrl-5>", "tab-focus 5", mode="command")
config.bind("<Ctrl-6>", "tab-focus 6", mode="command")
config.bind("<Ctrl-7>", "tab-focus 7", mode="command")
config.bind("<Ctrl-8>", "tab-focus 8", mode="command")
config.bind("<Ctrl-9>", "tab-focus 9", mode="command")
config.bind("<Ctrl-n>", "open -w", mode="command")
config.bind("<Ctrl-w>", "tab-close", mode="command")
config.bind("<Return>", "hint-follow", mode="hint")
config.bind("<Alt-Space>", "edit-text", mode="insert")
config.bind("<Ctrl-0>", "tab-focus 10", mode="insert")
config.bind("<Ctrl-1>", "tab-focus 1", mode="insert")
config.bind("<Ctrl-2>", "tab-focus 2", mode="insert")
config.bind("<Ctrl-3>", "tab-focus 3", mode="insert")
config.bind("<Ctrl-4>", "tab-focus 4", mode="insert")
config.bind("<Ctrl-5>", "tab-focus 5", mode="insert")
config.bind("<Ctrl-6>", "tab-focus 6", mode="insert")
config.bind("<Ctrl-7>", "tab-focus 7", mode="insert")
config.bind("<Ctrl-8>", "tab-focus 8", mode="insert")
config.bind("<Ctrl-9>", "tab-focus 9", mode="insert")
config.bind("<Ctrl-n>", "open -w", mode="insert")
config.bind("<Ctrl-w>", "tab-close", mode="insert")
config.bind(" n", "tab-move +", mode="normal")
config.bind(" p", "tab-move -", mode="normal")
config.bind(" w", "tab-close", mode="normal")
config.bind("+", "zoom-in", mode="normal")
config.bind("-", "zoom-out", mode="normal")
config.bind("0", "tab-focus 10", mode="normal")
config.bind("1", "tab-focus 1", mode="normal")
config.bind("2", "tab-focus 2", mode="normal")
config.bind("3", "tab-focus 3", mode="normal")
config.bind("4", "tab-focus 4", mode="normal")
config.bind("5", "tab-focus 5", mode="normal")
config.bind("6", "tab-focus 6", mode="normal")
config.bind("7", "tab-focus 7", mode="normal")
config.bind("8", "tab-focus 8", mode="normal")
config.bind("9", "tab-focus 9", mode="normal")
config.bind(":", "cmd-set-text :", mode="normal")
config.bind("<Alt-Space>", "hint images current", mode="normal")
config.bind("<Alt-x>", "forward", mode="normal")
config.bind("<Alt-z>", "back", mode="normal")
config.bind("<Ctrl-0>", "tab-focus 10", mode="normal")
config.bind("<Ctrl-1>", "tab-focus 1", mode="normal")
config.bind("<Ctrl-2>", "tab-focus 2", mode="normal")
config.bind("<Ctrl-3>", "tab-focus 3", mode="normal")
config.bind("<Ctrl-4>", "tab-focus 4", mode="normal")
config.bind("<Ctrl-5>", "tab-focus 5", mode="normal")
config.bind("<Ctrl-6>", "tab-focus 6", mode="normal")
config.bind("<Ctrl-7>", "tab-focus 7", mode="normal")
config.bind("<Ctrl-8>", "tab-focus 8", mode="normal")
config.bind("<Ctrl-9>", "tab-focus 9", mode="normal")
config.bind("<Ctrl-Alt-p>", "print", mode="normal")
config.bind("<Ctrl-Down>", "hint links download", mode="normal")
config.bind("<Ctrl-Left>", "tab-move -", mode="normal")
config.bind("<Ctrl-Right>", "tab-move +", mode="normal")
config.bind("<Ctrl-n>", "open -w", mode="normal")
config.bind("<Ctrl-o>", "cmd-set-text :open {url:pretty}", mode="normal")
config.bind("<Ctrl-p>", "spawn --userscript qutepass", mode="normal")
config.bind("<Ctrl-w>", "tab-close", mode="normal")
config.bind("<Ctrl-x>", "hint images delete", mode="normal")
config.bind("<Ctrl-y>", "hint links yank", mode="normal")
config.bind("<Left>", "tab-prev", mode="normal")
config.bind("<Right>", "tab-next", mode="normal")
config.bind("<Space><Space>", "hint links current", mode="normal")
config.bind("<Space>c", "hint links tab-fg", mode="normal")
config.bind("<Space>d", "hint --rapid images tab-bg", mode="normal")
config.bind("<Space>f", "hint images tab-fg", mode="normal")
config.bind("<Space>s", "hint images tab-bg", mode="normal")
config.bind("<Space>v", "hint --rapid links tab-bg", mode="normal")
config.bind("<Space>x", "hint links tab-bg", mode="normal")
config.bind("<less>", "home", mode="normal")
config.bind("<tab>", "nop", mode="normal")
config.bind("@", "macro-run", mode="normal")
config.bind("X", "forward -t", mode="normal")
config.bind("Z", "back -t", mode="normal")
config.bind("aa", "cmd-set-text -s :quickmark-add {title} {url} ", mode="normal")
config.bind("ct", "tab-only", mode="normal")
config.bind("gd", "download", mode="normal")
config.bind("gf", "view-source", mode="normal")
config.bind("gh", "https://duckduckgo.com", mode="normal")
config.bind("i", "hint inputs", mode="normal")
config.bind("q", "tab-close", mode="normal")
config.bind("sd", "cmd-set-text :session-delete  ", mode="normal")
config.bind("sh", "session-load -c startpage", mode="normal")
config.bind("sl", "cmd-set-text :session-load", mode="normal")
config.bind("ss", "cmd-set-text :session-save", mode="normal")
config.bind("st", "session-load -c trader", mode="normal")
config.bind("sx", "session-load -c xxx", mode="normal")
config.bind("v", "hint links spawn /nix/store/6ra22f747m99v22p7kxp7597w3943fcc-mpv-with-scripts-0.37.0/bin/mpv --loop {hint-url}", mode="normal")
config.bind("wi", "inspector", mode="normal")
config.bind("wp", "open -w -- {clipboard}", mode="normal")
config.bind("x", "tab-next", mode="normal")
config.bind("z", "tab-prev", mode="normal")
# c.tabs.padding = {"bottom": 6, "left": 7, "right": 7, "top": 6}
config.load_autoconfig(True)
# config.source('/home/sorath/.config/qutebrowser/themes/distrotube.py')
c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}
c.auto_save.session = False
c.auto_save.interval = 4000
c.statusbar.position = 'top'
c.statusbar.show = "never"
c.qt.args = ['disable-logging', 'disable-reading-from-canvas']
