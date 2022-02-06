/*
 https://icpcarchive.ecs.baylor.edu/external/81/8178.pdf
 submission #2687558
 verdict: Accepted
 Runtime: 0.003
 2022-02-06
*/
#include <bits/stdc++.h>

using namespace std;

bool isLatinSquare(const vector<string>& M) {
    int n = M.size();
    for(int r{}; r < n; ++r) {
        for(int c{}; c < n; ++c) {
            auto row = M[r];
            auto row_count = std::count(row.begin(), row.end(), M[r][c]);
            if(row_count > 1) return 0;
            // check rest of column (go down in rows)
            for(int rp = r + 1; rp < n; ++rp) {
                if(M[rp][c] == M[r][c]) return 0;
            } // end row prime for
        } // end col for
    } // end row for
    return 1;
}

bool isReduced(const vector<string>& M) {
    // check first row to see if in sorted order
    auto sorted_row = M[0];
    std::sort(sorted_row.begin(), sorted_row.end());
    if(!std::equal(sorted_row.begin(), sorted_row.end(), M[0].begin())) return 0;
    // check first col too
    string fcol = "";
    for(int r{}; r < M[0].size(); ++r) {
        fcol += M[0][r];
    }
    string sorted_col = fcol;
    std::sort(sorted_col.begin(), sorted_col.end());
    if(sorted_col != fcol) return 0;
    return 1;

}

void print(const vector<string>& M) {
    for(const auto& row : M) {
        for(const auto& col : row)
            cout << col << " ";
        cout << endl;
    }
    cout << endl;
}

int main() {
    vector<vector<string>> A;
    // io
    string inp;
    int n;
    while(getline(cin, inp)) {
        n = stoi(inp);
        vector<string> B;
        for(int x{}; x < n; ++x) {
            getline(cin, inp);
            B.push_back(inp);
        } // end for
        A.push_back(B);
    } // end while

    for(const auto& M : A) {
        //print(M);
        bool isLatin = isLatinSquare(M);
        bool reduced = isReduced(M);
        if(isLatin and reduced) cout << "Reduced\n";
        else if(isLatin) cout << "Not Reduced\n";
        else cout << "No\n";
    }

    return 0;
}
