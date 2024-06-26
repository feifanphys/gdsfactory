"""Design of Experiment (DOE) with custom add_fiber_array function.

In this case add_fiber_array does not add labels.

You can use gf.add_labels.add_labels_to_ports.

"""

from __future__ import annotations

from functools import partial

import gdsfactory as gf

if __name__ == "__main__":
    c = gf.components.pack_doe(
        gf.components.straight,
        settings={"length": [5, 5]},
        function=partial(gf.routing.add_fiber_array, get_input_labels_function=None),
    )
    c = gf.add_labels.add_labels_to_ports(
        component=c, prefix="opt_te1550_", port_type="vertical_te"
    )
    print(len(c.labels))
    c.show()
