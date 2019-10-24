import sys

from isort import wrap_modes

if sys.version_info[1] > 5:
    from hypothesis_auto import auto_pytest_magic

    auto_pytest_magic(wrap_modes.grid, auto_allow_exceptions_=(ValueError,))
    auto_pytest_magic(wrap_modes.vertical, auto_allow_exceptions_=(ValueError,))
    auto_pytest_magic(wrap_modes.hanging_indent, auto_allow_exceptions_=(ValueError,))
    auto_pytest_magic(wrap_modes.vertical_hanging_indent, auto_allow_exceptions_=(ValueError,))
    auto_pytest_magic(wrap_modes.vertical_grid, auto_allow_exceptions_=(ValueError,))
    auto_pytest_magic(wrap_modes.vertical_grid_grouped, auto_allow_exceptions_=(ValueError,))
    auto_pytest_magic(
        wrap_modes.vertical_grid_grouped_no_comma, auto_allow_exceptions_=(ValueError,)
    )
    auto_pytest_magic(wrap_modes.noqa, auto_allow_exceptions_=(ValueError,))
