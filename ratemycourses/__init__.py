### tgMochiKit

import tgmochikit
from turbogears.widgets import register_static_directory, Widget, JSLink

tgmochikit.init(register_static_directory, version="1.4.2", xhtml=True, packed=True)

class TGMochiKit(Widget):
	def retrieve_javascript(self):
		jss = [JSLink("tgmochikit", path) for path in tgmochikit.get_paths()]
		return jss

mochikit = TGMochiKit()

### tgMochiKit
