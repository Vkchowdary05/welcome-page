/**
 * Lab Project 13: Welcome Webpage
 * Displays welcome message and current date using JavaScript.
 */

let useIsoFormat = false;

function getCurrentDateData() {
  const now = new Date();

  // Readable standard format: e.g. "Wednesday, November 18, 2026"
  const options = {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  };
  const readableDate = now.toLocaleDateString('en-US', options);

  // ISO Format: YYYY-MM-DD
  const isoDate = now.toISOString().split('T')[0];

  // Time format
  const timeString = now.toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: true
  });

  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || 'Local';

  return {
    now,
    readableDate,
    isoDate,
    timeString,
    tz,
    dayName: now.toLocaleDateString('en-US', { weekday: 'long' }),
    timestamp: now.getTime()
  };
}

function updateDateDisplay() {
  const data = getCurrentDateData();
  const dateElement = document.getElementById('current-date');
  const detailsElement = document.getElementById('formatted-details');
  const tzElement = document.getElementById('system-tz');
  const timestampTag = document.getElementById('timestamp-tag');

  if (dateElement) {
    // If ISO mode is toggled, show ISO, else readable date
    dateElement.textContent = useIsoFormat ? data.isoDate : data.readableDate;
  }

  if (detailsElement) {
    detailsElement.textContent = `Local Time: ${data.timeString} (${data.tz})`;
  }

  if (tzElement) {
    tzElement.textContent = data.tz;
  }

  if (timestampTag) {
    timestampTag.textContent = `Epoch: ${data.timestamp}`;
  }

  console.log('[DevOps Lab 13] Date refreshed:', data.readableDate, data.timeString);
}

function toggleDateFormat() {
  useIsoFormat = !useIsoFormat;
  updateDateDisplay();
}

// Initial execution on DOM content loaded
document.addEventListener('DOMContentLoaded', () => {
  console.log('[DevOps Lab 13] Welcome webpage initialized.');
  updateDateDisplay();
});
