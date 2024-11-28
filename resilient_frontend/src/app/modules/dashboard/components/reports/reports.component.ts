import { Component, OnInit } from '@angular/core';
import { User, Users, ReportType } from '../../../../shared/models/database-types';
import { DataStorageService } from '@app/services/data-storage.service';
import { ConfirmationService } from 'primeng/api';
import { RequestsService } from '@app/services/requests.service';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrl: './reports.component.scss'
})
export class ReportsComponent implements OnInit{

  filteredParticipants: User[] = [];
  participants: User[] = [];
  selectedParticipant: User | undefined;
  showDialog: boolean = false;
  username: string;
  usernameFilter: string = '';
  reportTypes = [
    {reportType: 'Weekly', value: 'one'},
    {reportType: 'Aggregated', value: 'all'},
  ]
  selectedReportType: ReportType | undefined;
  selectedRows: any[] = [];
  reports = [];
  filteredReports = [];
  maxColumnWidth: number = 200;
  selectedColumns: any[] = [];
  showReportDialog = false;
  pdfUrl: SafeResourceUrl | null = null;


  constructor(
    private _dataStorageService: DataStorageService,
    private _confirmationService: ConfirmationService,
    private _requestsService: RequestsService,
    private sanitizer: DomSanitizer,
    private _router: Router,
    private _route: ActivatedRoute,
  ) {
    this.username = '';
  }

  ngOnInit(): void {
    //this.getUsers();
    this._route.queryParamMap.subscribe(params => {
      const type = params.get('report_type');
      const user = params.get('username');
      console.log(type, user);

      this.generateReport(user, type);
    });
    this.getReports();
    this.calculateMaxColumnWidth();
    window.addEventListener('resize', this.calculateMaxColumnWidth.bind(this));
  }

  calculateMaxColumnWidth() {
    this.maxColumnWidth = 0.8 * window.innerWidth/(this.selectedColumns.length+1);
    document.documentElement.style.setProperty('--maxColumnWidth', this.maxColumnWidth + 'px');

  }

  getUsers(): void {
    this._dataStorageService.getUsers().subscribe({
      next: (filteredUsers: User[]) => {
        this.participants = filteredUsers;
        this.filteredParticipants = filteredUsers;
      },
      error: (err) => {
        console.error('Error fetching users:', err);
      }
    });
  }

  getReports(): void {
    this._dataStorageService.getReports().subscribe({
      next: (reports: any) => {
        this.reports = reports;
        this.filteredReports = reports;
        this.participants = reports.map((item: { username: any; }) => ({ username: item.username }));

        console.log(this.reports);

      }
    })
  }

  applyUsernameFilter(): void {
    this.filteredParticipants = this.participants.filter(participant => {
      return participant.username.toLowerCase().includes(this.usernameFilter.toLowerCase());
    });
  }

  showCreateReporttModal(): void {
    this.showDialog = true;
    if (this.usernameFilter) {
      this.username = this.usernameFilter
    }
  }

  generateReportConfirmation(event: Event): void {
    this._confirmationService.confirm({
      target: event.target as EventTarget,
      message: 'Do you want to generate a report for this participant?',
      header: 'Report Confirmation',
      icon: 'pi pi-file-pdf',
      acceptButtonStyleClass:"p-button-danger p-button-text",
      rejectButtonStyleClass:"p-button-text p-button-text",
      acceptIcon:"none",
      rejectIcon:"none",

      accept: () => {
        this.generateReport(this.selectedParticipant!.username, this.selectedReportType!.value);
      },
      reject: () => {}
    });
  }

  generateReport(username: string | null = '', reportType: string | null  = ''): void {
    username = username ? username : this.selectedParticipant!.username;
    reportType = reportType ? reportType : this.selectedReportType!.value;
    this._requestsService.generateReport(username, reportType).subscribe({
      next: (response) => {
        console.log('Response received:', response);
        const blob = new Blob([response], { type: 'application/pdf' });
        const objectUrl = URL.createObjectURL(blob);
        this.pdfUrl = this.sanitizer.bypassSecurityTrustResourceUrl(objectUrl); // Sanitize the URL
        this.showReportDialog = true;
      },
      error: (error) => {
        console.error('Failed to generate report:', error);
      },
      complete: () => {
        console.log('Request completed.');
      }
    });
  }

  onDialogHide(): void {
    if (this.pdfUrl) {
      this.pdfUrl = null;
    }
  }

  closeParticipants() {
    //Go to /dashboard
    this._router.navigate(['/dashboard']);
  }


  onSelectReport(participant: any): void {}



}
