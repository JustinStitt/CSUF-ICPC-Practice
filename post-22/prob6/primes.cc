#include <bits/stdc++.h>

using namespace std;

vector<int> sieve(int min = 2, int max = 1299799) { // change max to be a bit bigger then clamp possible to 100,000
	vector<int> possible;
	for(int x = min; x <= max; ++x) {
		possible.push_back(x);
	}
	
	for(int i = min; i < max; ++i) {
		for(int j = i*2; j < max; j+=i) {
			possible[j-2] = 0;
		}
	}

	vector<int> primes;
	for(auto& c	 : possible) {
		if(c == 0) continue;
		primes.push_back(c);
		if(primes.size() >= 100000) break;
	}
	return primes;
}

uint64_t solve(int i, int j, string k, const vector<int>& primes) {
	uint64_t total = 0;
	for(int x = i-1; x < j; ++x) {
		string inquiry = to_string(primes[x]);
		auto f = inquiry.find(k);
		if(f != string::npos) total += 1;
	}
	return total;
}

int main() {
	
	int i, j;
	string k;
	vector<int> primes = sieve();
	while(cin >> i >> j) {
		cin >> k;
		uint64_t result = solve(i, j, k, primes);
		cout << result << "\n";
	}
	
	return 0;
}
