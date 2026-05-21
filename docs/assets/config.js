window.BOOK_CONFIG = {
  repoUrl: 'https://github.com/pkolekar/agentic_ai_for_cancer_research',
  defaultBranch: 'main',
  theme: 'clinical-journal',
  notebookViewer: 'nbviewer'
};

window.BOOK_THEMES = [
  'clinical-journal',
  'data-atlas',
  'lab-notebook',
  'material-docs',
  'sphinx-classic'
];

function resolveInitialTheme() {
  const configured = (window.BOOK_CONFIG && window.BOOK_CONFIG.theme) || 'clinical-journal';
  try {
    const stored = localStorage.getItem('book-theme');
    if (stored && window.BOOK_THEMES.includes(stored)) {
      return stored;
    }
  } catch (error) {
    // localStorage may be unavailable in private or restricted contexts.
  }
  return window.BOOK_THEMES.includes(configured) ? configured : 'clinical-journal';
}

window.applyBookTheme = function applyBookTheme(themeName) {
  const safeTheme = window.BOOK_THEMES.includes(themeName) ? themeName : 'clinical-journal';
  document.documentElement.setAttribute('data-theme', safeTheme);
  try {
    localStorage.setItem('book-theme', safeTheme);
  } catch (error) {
    // Ignore storage failures and still apply theme for this session.
  }
  return safeTheme;
};

window.setupThemePicker = function setupThemePicker(elementId) {
  const picker = document.getElementById(elementId);
  if (!picker) {
    return;
  }
  const current = document.documentElement.getAttribute('data-theme') || 'clinical-journal';
  picker.value = current;
  picker.addEventListener('change', (event) => {
    const selected = window.applyBookTheme(event.target.value);
    picker.value = selected;
  });
};

(function initConfiguredTheme() {
  window.applyBookTheme(resolveInitialTheme());
})();
