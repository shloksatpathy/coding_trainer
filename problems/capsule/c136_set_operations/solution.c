#include <stdio.h>
#include <stdlib.h>

int a[1000], b[1000], out[2000];

int compare(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    return (x > y) - (x < y);
}

int read_set(int v[]) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    qsort(v, n, sizeof v[0], compare);
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || v[i] != v[i - 1]) {
            v[k++] = v[i];
        }
    }
    return k;
}

void show(const char *label, int v[], int k) {
    printf("%s:", label);
    if (k == 0) {
        printf(" none");
    }
    for (int i = 0; i < k; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");
}

int main(void) {
    int n = read_set(a), m = read_set(b);
    int i, j, k;
    k = 0;
    for (i = 0, j = 0; i < n || j < m; k++) {
        if (j == m || (i < n && a[i] < b[j])) {
            out[k] = a[i++];
        } else if (i == n || b[j] < a[i]) {
            out[k] = b[j++];
        } else {
            out[k] = a[i++];
            j++;
        }
    }
    show("union", out, k);
    k = 0;
    for (i = 0, j = 0; i < n && j < m;) {
        if (a[i] < b[j]) {
            i++;
        } else if (b[j] < a[i]) {
            j++;
        } else {
            out[k++] = a[i++];
            j++;
        }
    }
    show("both", out, k);
    k = 0;
    for (i = 0, j = 0; i < n; ) {
        if (j == m || a[i] < b[j]) {
            out[k++] = a[i++];
        } else if (b[j] < a[i]) {
            j++;
        } else {
            i++;
            j++;
        }
    }
    show("only first", out, k);
    return 0;
}
