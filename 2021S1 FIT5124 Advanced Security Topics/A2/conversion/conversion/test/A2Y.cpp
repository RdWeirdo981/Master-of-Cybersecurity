//
// Created by shangqi on 2021/1/28.
//
#include <iostream>

#include "secret_sharing/secret_sharing.h"

using namespace emp;
using namespace std;

// convert the secret input of the designated additive party to Yao's share
Integer A2Y(AdditiveParty<NetIO> additiveParty, int party) {
    // Generate the label for share 0, share 1 and field size (2^32)
    Integer share_0(64, additiveParty.get_share(party), ALICE);
    Integer share_1(64, additiveParty.get_share(party), BOB);
    Integer MOD(64, (long) 1 << 32, PUBLIC);
    // we can directly use the % operator here because the share is already a non-negative number
    return (share_0 + share_1) % MOD;
}

int main(int argc, char** argv) {
    // create channel
    int port, party;
    parse_party_and_port(argv, &party, &port);
    auto * io_Alice = new NetIO(party==ALICE ? nullptr : "127.0.0.1", port);
    auto * io_Bob = new NetIO(party==BOB ? nullptr : "127.0.0.1", port + 1);
    // setup parties, the private input is the third parameter
    auto entity = setup_additive_party(party, io_Alice, io_Bob, atoi(argv[3]));
    entity.share();
    setup_semi_honest(io_Alice, party);
    Integer alice_input = A2Y(entity, BOB);
    cout << alice_input.reveal<int32_t>() << endl;
    delete io_Alice;
    delete io_Bob;
}