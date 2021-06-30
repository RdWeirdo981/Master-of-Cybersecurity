//
// Created by shangqi on 2021/1/28.
//
#include <iostream>

#include "secret_sharing/secret_sharing.h"

using namespace emp;
using namespace std;

// convert the secret input of the designated additive party to Yao's share
void Y2A(Integer share, int share_party, int current_party) {
    // Generate a local random number as share_0
    long random{};
    PRG shared_prg;
    shared_prg.random_data((void *) &random, sizeof(int));
    Integer share_0(64, random, share_party);
    Integer MOD(64, (long) 1 << 32, PUBLIC);
    // evaluate the new share
    Integer share_1 = ((share - share_0) % MOD + MOD) % MOD;
    // the share is generated
    // the owner of this secret value keeps random (i.e, the random generated value share_0)
    if(share_party == current_party) {
        cout << random << endl;
    }
    // the counter party should keep share_1 which is revealed at the end of the evaluation
    cout << share_1.reveal<int64_t>() << endl;
    // you should use the above two values as the additive shares for further computation
}

int main(int argc, char** argv) {
    // create channel
    int port, party;
    parse_party_and_port(argv, &party, &port);
    auto * io_Alice = new NetIO(party==ALICE ? nullptr : "127.0.0.1", port);
    auto * io_Bob = new NetIO(party==BOB ? nullptr : "127.0.0.1", port + 1);
    setup_semi_honest(io_Alice, party);
    Integer input(64, atoi(argv[3]), ALICE);
    // convert the Yao's share two additive shares
    Y2A(input, ALICE, party);
    //cout << alice_input.reveal<int32_t>() << endl;
    delete io_Alice;
    delete io_Bob;
}