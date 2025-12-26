import { useState } from "react";
import { checkWeakPasswd } from "./passwd_checker";

const RULES = [
  "At least 8 characters",
  "Contains uppercase letter",
  "Contains lowercase letter",
  "Contains number",
  "Contains special symbol"
];

export default function PasswordStrengthUI() {
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const errors = password ? checkWeakPasswd(password) : [];

  // Calculate how many rules passed
  const passedCount = RULES.length - errors.length;

  return (
    <div className="min-h-screen bg-slate-950 text-white font-sans flex items-center justify-center">
      <main className="w-full max-w-md px-6 py-8">

        {/* Header */}
        <div className="text-center mb-8">
          <h2 className="text-3xl font-extrabold mb-2">Test your security</h2>
          <p className="text-slate-400">
            Enter a password to analyze its strength and complexity.
          </p>
        </div>

        {/* Password Input */}
        <div className="relative group mb-6">
          <div className="absolute -inset-0.5 bg-gradient-to-r from-emerald-500/50 to-emerald-400/50 rounded-2xl blur opacity-30"></div>
          <div className="relative flex items-center bg-slate-800 border border-slate-700 rounded-xl p-1">
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Type a password..."
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-transparent px-4 py-3 text-xl outline-none text-white"
            />
            <button
              onClick={() => setShowPassword(!showPassword)}
              className="px-4 text-slate-400 hover:text-emerald-400"
            >
              {showPassword ? "👁️" : "👁️‍🗨️"}
            </button>
          </div>
        </div>

        {password && (
          <>
            {/* Strength Meter */}
            <div className="mb-6">
              <div className="flex justify-between mb-2">
                <span className="text-sm text-slate-400">Strength</span>
                <span className={`text-sm font-bold ${
                  passedCount === RULES.length ? "text-emerald-400" : "text-slate-400"
                }`}>
                  {passedCount === RULES.length ? "Strong" : "Weak"}
                </span>
              </div>

              <div className="flex gap-2 h-2">
                {RULES.map((_, i) => (
                  <div
                    key={i}
                    className={`flex-1 rounded-full transition-all ${
                      i < passedCount
                        ? "bg-emerald-400 shadow-[0_0_10px_rgba(52,211,153,0.5)]"
                        : "bg-slate-700"
                    }`}
                  />
                ))}
              </div>
            </div>

            {/* Requirements Checklist */}
            <div className="bg-slate-800/50 rounded-2xl p-5 border border-slate-700">
              <h3 className="text-xs font-bold uppercase text-slate-500 mb-4">
                Requirements
              </h3>

              <ul className="space-y-4">
                {RULES.map((rule) => {
                  const failed = errors.includes(rule);
                  return (
                    <li key={rule} className="flex items-center gap-3">
                      <span
                        className={`w-6 h-6 flex items-center justify-center rounded-full text-sm font-bold ${
                          failed
                            ? "bg-slate-700 text-slate-500"
                            : "bg-emerald-400/20 text-emerald-400"
                        }`}
                      >
                        {failed ? "○" : "✓"}
                      </span>
                      <span
                        className={`text-sm ${
                          failed
                            ? "text-slate-500"
                            : "text-white font-medium"
                        }`}
                      >
                        {rule}
                      </span>
                    </li>
                  );
                })}
              </ul>
            </div>
          </>
        )}

        {/* Action Button */}
        <div className="mt-8">
          <button
            onClick={() => {
              if (password) {
                navigator.clipboard.writeText(password);
                alert('Password copied to clipboard!');
              }
            }}
            disabled={!password}
            className="w-full h-14 bg-emerald-400 disabled:bg-slate-700 disabled:text-slate-500 text-slate-950 font-bold text-lg rounded-xl transition-all flex items-center justify-center gap-2"
          >
            <span>📋</span>
            Copy Password
          </button>
        </div>

      </main>
    </div>
  );
}