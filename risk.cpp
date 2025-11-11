#include <iostream>
#include <cmath>
using namespace std;

string solve(long long N, long long M) {
    // Filippo wins if M >= N - ceil(N/3) + 2
    // Tommaso wins if N >= M - ceil(M/3) + 2
    // Otherwise draw
    
    long long filippo_threshold = N - (N + 2) / 3 + 2;
    long long tommaso_threshold = M - (M + 2) / 3 + 2;
    
    if (M >= filippo_threshold) {
        return "filippo";
    } else if (N >= tommaso_threshold) {
        return "tommaso";
    } else {
        return "draw";
    }
}

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        long long N, M;
        cin >> N >> M;
        cout << solve(N, M) << endl;
    }
    
    return 0;
}
