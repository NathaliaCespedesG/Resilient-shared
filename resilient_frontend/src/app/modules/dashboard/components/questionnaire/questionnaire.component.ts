import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrl: './questionnaire.component.scss'
})
export class QuestionnaireComponent {

  // User Type Selection
  userTypes = [
    { label: 'GP', value: 'GP' },
    { label: 'Participant', value: 'Participant' },
  ];
  selectedUserType: string | null = this.userTypes[0].value;

  // GP Questions
  gpQualityCareOptions = [
    'Diagnosis',
    'Identify Patient at Risk',
    'Defining Treatment Plan',
    'Suggesting Treatment',
    'Prevention',
    'Prevented Hospital re-admission',
    'Medication choice',
    'Medication change',
    'Manage Chronic Illness',
    'No',
    'Other (Specify)',
  ];
  selectedGpQualityCare: string[] = [];

  gpEfficiencyRating: number = 0;
  additionalNotesGp: string = '';

  gpKeyMessages = [
    'Improved communication with patient',
    'Delayed decision making',
    'Improved decision making',
    'Reduced time spent on administrative tasks',
    'Saved time during follow-up',
    'Facilitated clearer communication with patient',
    'Decreased follow-up appointment frequency',
    'Improved patient data accessibility',
    'Less diagnostic test ordered',
    'More diagnostic test ordered',
    'Other (Specify)',
  ];
  selectedGpKeyMessages: string[] = [];

  // Participant Questions
  participantHealthReportFrequency = [
    { label: 'Once a weekly', value: 'Once a weekly' },
    { label: 'Once a month', value: 'Once a month' },
    { label: 'Each three months', value: 'Each three months' },
    { label: 'Rarely', value: 'Rarely' },
    { label: 'Never', value: 'Never' },
  ];
  selectedParticipantHealthReportFrequency: string | null = null;

  participantReportUsageOptions = [
    'To monitor my health trends',
    'To track progress over time',
    'To share with my healthcare provider for additional insight',
    'To adjust my health habits',
    'I don’t use the report for any specific purpose',
  ];
  selectedParticipantReportUsage: string | null = null;

  participantHealthHelpfulness = [
    'Extremely helpful',
    'Very helpful',
    'Somewhat helpful',
    'Not very helpful',
    'Not helpful at all',
  ];
  selectedParticipantHealthHelpfulness: string | null = null;

  constructor (
    private _router: Router,
  ) {}

  closeQuestionnaire() {
    console.log(this.selectedUserType);

    //Go to /dashboard
    this._router.navigate(['/dashboard']);
  }

  onUserTypeChange(event: any): void {
    console.log('Selected User Type:', this.selectedUserType); // Debugging value
  }


}
