# Script used to test the network with batfish

from pybatfish.client.commands import *
from pybatfish.question import load_questions
from pybatfish.client.asserts import (
    assert_no_duplicate_router_ids,
    assert_no_incompatible_bgp_sessions,
    assert_no_incompatible_ospf_sessions,
    assert_no_unestablished_bgp_sessions,
    assert_no_undefined_references,
)
from rich import print as rprint
from rich.console import Console

console = Console(color_system="truecolor")


def test_duplicate_rtr_ids(snap):
    """Testing for duplicate router IDs"""
    console.print(
        ":red_exclamation_mark: [bold yellow]Testing for duplicate router IDs[/bold yellow] :red_exclamation_mark:"
    )
    assert_no_duplicate_router_ids(
        snapshot=snap,
        protocols={"ospf", "bgp"},
    )
    console.print(
        ":green_heart: [bold green]No duplicate router IDs found[/bold green] :green_heart:"
    )


def main():
    """init all the things"""
    NETWORK_NAME = "MASTRO_TESTNET"
    SNAPSHOT_NAME = "snapshot00"
    SNAPSHOT_DIR = "./snapshots"
    bf_session.host = "192.168.69.13"
    bf_set_network(NETWORK_NAME)
    init_snap = bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)
    load_questions()
    test_duplicate_rtr_ids(init_snap)
    # test_bgp_compatibility(init_snap)
    # test_ospf_compatibility(init_snap)
    # test_bgp_unestablished(init_snap)
    # test_undefined_references(init_snap)


if __name__ == "__main__":
    main()
