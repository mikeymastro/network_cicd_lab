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
    ### Testing for duplicate router IDs ###
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for duplicate router IDs[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_duplicate_router_ids(
        snapshot=snap,
        protocols={"ospf", "bgp"},
    )
    console.print(
        ":green_heart: [bold green]No duplicate router IDs found[/bold green] :green_heart:"
    )


def test_bgp_compatibility(snap):
    ### Testing for incompatible BGP sessions ###
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for Incompatible BGP Sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_incompatible_bgp_sessions(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]All BGP Sessions Compatible[/bold green] :green_heart:"
    )


def test_ospf_compatibility(snap):
    ### Testing for incompatible OSPF sessions ###
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for Incompatible OSPF Sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_incompatible_ospf_sessions(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]All OSPF Sessions Compatible[/bold green] :green_heart:"
    )


def test_bgp_unestablished(snap):
    ### Testing for BGP sessions that are not established ###
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for Unestablished BGP Sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_unestablished_bgp_sessions(
        snapshot=snap,
        soft=True,
    )
    console.print(
        ":green_heart: [bold green]All BGP Sessions Established[/bold green] :green_heart:"
    )


def test_undefined_references(snap):
    ### Testing for any undefined references ###
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for Undefined References[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_undefined_references(
        snapshot=snap,
        soft=True,
    )
    console.print(
        ":green_heart: [bold green]No Undefined References Found[/bold green] :green_heart:"
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
    test_bgp_compatibility(init_snap)
    test_ospf_compatibility(init_snap)
    test_bgp_unestablished(init_snap)
    test_undefined_references(init_snap)


if __name__ == "__main__":
    main()
