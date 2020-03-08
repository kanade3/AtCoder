#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int H, W, K, A[309][309], num;
int cnt[309];
char c[309][309];

void solve(int cl, int cr) {
	vector<int> P;
	for (int i = cl; i <= cr; i++) {
		for (int j = 1; j <= W; j++) {
			if (c[i][j] == '#') P.push_back(j);
		}
	}
	sort(P.begin(), P.end());

	for (int i = 0; i < P.size(); i++) {
		int v1 = 1, v2 = W;
		if (i >= 1) v1 = P[i - 1] + 1;
		if (i < (int)P.size() - 1) v2 = P[i];

		num++;
		for (int j = cl; j <= cr; j++) {
			for (int k = v1; k <= v2; k++) A[j][k] = num;
		}
	}
}

int main() {
	cin >> H >> W >> K;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			cin >> c[i][j];
			if (c[i][j] == '#') cnt[i]++;
		}
	}

	vector<int> vec;
	for (int i = 1; i <= H; i++) { if (cnt[i] >= 1) vec.push_back(i); }
	for (int i = 0; i < vec.size(); i++) {
		int v1 = 1, v2 = H;
		if (i >= 1) v1 = vec[i - 1] + 1;
		if (i < (int)vec.size() - 1) v2 = vec[i];

		solve(v1, v2);
	}

	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			if (j >= 2) cout << " "; cout << A[i][j];
		}
		cout << endl;
	}
	return 0;
}
