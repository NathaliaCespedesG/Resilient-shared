#!/bin/sh

# Create the env.js file with the environment variables
echo "window.__env = {" > /usr/share/nginx/html/browser/assets/env.js
echo "  apiUrl: \"$API_URL\"," >> /usr/share/nginx/html/browser/assets/env.js
echo "  chartFields: {" >> /usr/share/nginx/html/browser/assets/env.js
echo "    scale: [" >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'weight', label: 'Weight', units: 'kg' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'bone_mass', label: 'Bone Mass', units: 'kg' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'muscle_mass', label: 'Muscle Mass', units: 'kg' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'fat_mass', label: 'Fat Mass', units: 'kg' }" >> /usr/share/nginx/html/browser/assets/env.js
echo "    ]," >> /usr/share/nginx/html/browser/assets/env.js
echo "    scan_watch: [" >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'average_heart_rate', label: 'Av. Heart Rate', units: 'bpm' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'calories', label: 'Calories', units: 'kcal' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'steps', label: 'Steps', units: 'steps' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'hr_max', label: 'Max Heart Rate', units: 'bpm' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'hr_min', label: 'Min Heart Rate', units: 'bpm' }" >> /usr/share/nginx/html/browser/assets/env.js
echo "    ]," >> /usr/share/nginx/html/browser/assets/env.js
echo "    sleep_mat: [" >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'breathing_disturbances', label: 'Breathing Disturbances', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'deep_sleep_duration', label: 'Deep Sleep', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'light_sleep_duration', label: 'Light Sleep', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'rem_sleep_duration', label: 'REM Sleep', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'duration_to_sleep', label: 'Duration to Sleep', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'duration_to_wakeup', label: 'Duration to Wake Up', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'average_heart_rate', label: 'Av. Heart Rate', units: 'bpm' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'average_rr', label: 'Av. Respiration Rate', units: 'bpm' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'sleep_score', label: 'Sleep Score', units: 'score' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'wakeup_count', label: 'Wakeup Count', units: 'count' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'wakeup_duration', label: 'Wakeup Duration', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'apnea', label: 'Apnea', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'awake_in_bed', label: 'Awake in Bed', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'out_of_bed_count', label: 'Out of Bed Count', units: 'count' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'total_sleep_time', label: 'Total Sleep Time', units: 'min' }," >> /usr/share/nginx/html/browser/assets/env.js
echo "      { fieldName: 'total_time_in_bed', label: 'Total Time in Bed', units: 'min' }" >> /usr/share/nginx/html/browser/assets/env.js
echo "    ]" >> /usr/share/nginx/html/browser/assets/env.js
echo "  }," >> /usr/share/nginx/html/browser/assets/env.js
echo "  nullReplaceValue: $NULL_REPLACE_VALUE," >> /usr/share/nginx/html/browser/assets/env.js
echo "  withingsAuthUrl: \"$WITHINGS_AUTH_URL\"" >> /usr/share/nginx/html/browser/assets/env.js
echo "};" >> /usr/share/nginx/html/browser/assets/env.js

# Start Nginx
nginx -g 'daemon off;'
