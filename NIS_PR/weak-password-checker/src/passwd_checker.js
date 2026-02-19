export function checkWeakPasswd(passwd) {
    const rules = [
        {
            message: "At least 8 characters",
            test: (passwd) => passwd.length >= 8
            /* lemon code for above line of code...
            *  function (passwd) {
            *       return pwd.length >= 8;
            *   } 
            */
        },
        {
            message: "Contains uppercase letter",
            test: (passwd) => /[A-Z]/.test(passwd)
        },
        {
            message: "Contains lowercase letter",
            test: (passwd) => /[a-z]/.test(passwd)
        },
        {
            message: "Contains number",
            test: (passwd) => /[0-9]/.test(passwd)
        },
        {
            message: "Contains special symbol",
            test: (passwd) => /[!@#$%^&*]/.test(passwd)
        }
    ];

    return rules
        .filter(rule => !rule.test(passwd))
        .map(rule => rule.message);
}