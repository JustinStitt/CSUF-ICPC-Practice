#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	if(n&1) {
		cout << "still running\n";
		return 0;
	}
	vector<int> btns(n);
	for(int x{}; x < n; ++x) {
		cin >> btns[x];
	}

	bool on = 0;
	int lp{}, elap{};
	for(auto&& press : btns) {
		on = !on;
		if(!on) {
			elap += press - lp;
			continue;
		}
		lp = press;
	}

	cout << elap << "\n";

	return 0;
}