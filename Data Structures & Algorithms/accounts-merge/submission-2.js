class LinkedAccounts {
    constructor(accounts) {
        this.numAccounts = accounts.length;
        this.parentAccount = {}
        this.rank = {}
        //initialize parent map for each account i
        for (let i = 0; i < this.numAccounts; i++) {
            this.parentAccount[i] = i;
            this.rank[i] = accounts[i].length;
        }
    }

    findRootAccount(acct) {
        if (this.parentAccount[acct] == acct) {
            return acct;
        }
        const rootAcct = this.findRootAccount(this.parentAccount[acct]);
        //assign
        this.parentAccount[acct] = rootAcct;
        //return root for upstream rec calls
        return rootAcct;
    }

    mergeAccounts(a1, a2) {
        const r1 = this.findRootAccount(a1);
        const r2 = this.findRootAccount(a2);
        if (r1 == r2) {
            
            //means that there was another dup
            this.rank[r1] -= 1;
            return;
        }
        if (this.rank[r1] > this.rank[r2]) {
            this.parentAccount[r2] = r1;
            this.rank[r1] += this.rank[r2]
        } else if (this.rank[r2] >= this.rank[r1]) {
            this.parentAccount[r1] = r2;
            this.rank[r2] += this.rank[r1]
        }
    }
}
class Solution {
    /**
     * @param {string[][]} accounts
     * @return {string[][]}
     */
    accountsMerge(accounts) {
        console.log("starting")
        //initialize accounts list 
        const linkedAccounts = new LinkedAccounts(accounts);
        
        //1a. associate each email with an account
        //1b. map accts to each other
        //map email to account idx => if idx already exists, then merge the accts
        const emailToAcct = new Map();
        for (let acct_i = 0; acct_i < accounts.length; acct_i++) {
            //skip name bc if matching email we want to merge else no
            const acct = accounts[acct_i];
            for (let mail_i = 1; mail_i < acct.length; mail_i++) {
                const mail = acct[mail_i]
                //console.log("email mapping: ", emailToAcct)
                //check if email is already in emailToAcct
                if (emailToAcct.has(mail)) {
                    //merge that acct with this acct
                    const otherAcct_i = emailToAcct.get(mail);
                    //merge acct with it
                    //console.log("merging: ", otherAcct_i, acct_i)
                    linkedAccounts.mergeAccounts(otherAcct_i, acct_i);
                    //console.log(linkedAccounts.parentAccount);
                } else {
                    //associate with an acct for later
                    emailToAcct.set(mail, acct_i)
                    //console.log("email mapping: ", mail, acct_i)
                }
            }
        }
        console.log(linkedAccounts.parentAccount)
        console.log(linkedAccounts.rank)
        console.log(emailToAcct)
        const unique_accts = new Map();
        for (const [email, linked_acct] of emailToAcct) {
            const root_acct = linkedAccounts.findRootAccount(linked_acct);
            //console.log("email: ", email, " linked acct: ", linked_acct)
            if (!unique_accts.has(root_acct)) {
                unique_accts.set(root_acct, []);
            }
            unique_accts.get(root_acct).push(email);
            //console.log(unique_accts)
        }

        const result = []
        for (const [root_acct, emails] of unique_accts) {
            emails.sort();
            //insert name in front
            emails.unshift(accounts[root_acct][0]);
            result.push(emails);
        }
        return result;
    }
}
