from elmada._version import __version__

from .mode import get_mode, set_mode

from . import (
    el_entsoepy,
    el_EU_PWL_CEFs,
    el_geo_morph,
    el_opsd,
    el_other,
    el_share_CCGT,
    el_smard,
    geo_scraper,
    helper,
    paths,
    plots,
)

from .main import (
    get_el_national_generation,
    get_emissions,
    get_merit_order,
    get_prices,
    get_residual_load,
)
