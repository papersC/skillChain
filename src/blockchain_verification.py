"""
SkillChain DX - Blockchain Credential Verification Module
Lightweight implementation using SHA-256 hashing and local ledger
"""

import hashlib
import json
import datetime
from typing import Dict, List, Optional
from pathlib import Path


class CredentialLedger:
    """Simple blockchain-inspired credential verification system"""
    
    def __init__(self, ledger_path: str = 'data/credential_ledger.json'):
        """
        Initialize the credential ledger
        
        Args:
            ledger_path: Path to store the ledger file
        """
        self.ledger_path = ledger_path
        self.ledger = self._load_ledger()
        
    def _load_ledger(self) -> Dict:
        """Load existing ledger or create new one"""
        ledger_file = Path(self.ledger_path)
        
        if ledger_file.exists():
            with open(self.ledger_path, 'r') as f:
                return json.load(f)
        else:
            return {
                'credentials': [],
                'metadata': {
                    'created_at': datetime.datetime.now().isoformat(),
                    'version': '1.0',
                    'description': 'SkillChain DX Credential Ledger'
                }
            }
    
    def _save_ledger(self):
        """Save ledger to file"""
        Path(self.ledger_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.ledger_path, 'w') as f:
            json.dump(self.ledger, f, indent=2)
    
    def _compute_hash(self, data: Dict) -> str:
        """
        Compute SHA-256 hash of credential data
        
        Args:
            data: Credential data dictionary
            
        Returns:
            Hexadecimal hash string
        """
        # Create canonical string representation
        canonical_string = json.dumps(data, sort_keys=True)
        
        # Compute SHA-256 hash
        hash_object = hashlib.sha256(canonical_string.encode())
        return hash_object.hexdigest()
    
    def issue_credential(self, employee_id: str, course_id: str, 
                        course_name: str, completion_date: str,
                        issuer: str = 'SkillChain DX Platform') -> Dict:
        """
        Issue a new credential and add to ledger
        
        Args:
            employee_id: Employee identifier
            course_id: Course identifier
            course_name: Name of the course
            completion_date: Date of completion
            issuer: Credential issuer
            
        Returns:
            Credential record with hash
        """
        # Create credential data
        credential_data = {
            'employee_id': employee_id,
            'course_id': course_id,
            'course_name': course_name,
            'completion_date': completion_date,
            'issuer': issuer
        }
        
        # Compute hash
        credential_hash = self._compute_hash(credential_data)
        
        # Create full credential record
        credential_record = {
            'credential_id': f"CRED_{len(self.ledger['credentials']) + 1:04d}",
            'timestamp': datetime.datetime.now().isoformat(),
            'data': credential_data,
            'hash': credential_hash,
            'status': 'active'
        }
        
        # Add to ledger
        self.ledger['credentials'].append(credential_record)
        self._save_ledger()
        
        print(f"✓ Credential issued: {credential_record['credential_id']}")
        print(f"  Hash: {credential_hash[:16]}...")
        
        return credential_record
    
    def verify_credential(self, employee_id: str, course_id: str, 
                         course_name: str, completion_date: str,
                         issuer: str = 'SkillChain DX Platform') -> Dict:
        """
        Verify if a credential exists in the ledger
        
        Args:
            employee_id: Employee identifier
            course_id: Course identifier
            course_name: Name of the course
            completion_date: Date of completion
            issuer: Credential issuer
            
        Returns:
            Verification result dictionary
        """
        # Create credential data to verify
        credential_data = {
            'employee_id': employee_id,
            'course_id': course_id,
            'course_name': course_name,
            'completion_date': completion_date,
            'issuer': issuer
        }
        
        # Compute hash
        verification_hash = self._compute_hash(credential_data)
        
        # Search ledger
        for record in self.ledger['credentials']:
            if record['hash'] == verification_hash and record['status'] == 'active':
                return {
                    'verified': True,
                    'credential_id': record['credential_id'],
                    'timestamp': record['timestamp'],
                    'hash': verification_hash,
                    'message': 'Credential verified successfully'
                }
        
        return {
            'verified': False,
            'hash': verification_hash,
            'message': 'Credential not found in ledger'
        }
    
    def get_employee_credentials(self, employee_id: str) -> List[Dict]:
        """
        Get all credentials for an employee
        
        Args:
            employee_id: Employee identifier
            
        Returns:
            List of credential records
        """
        credentials = []
        for record in self.ledger['credentials']:
            if (record['data']['employee_id'] == employee_id and 
                record['status'] == 'active'):
                credentials.append(record)
        
        return credentials
    
    def generate_verification_report(self, output_path: str = 'results/verification_report.json'):
        """Generate verification report for all credentials"""
        report = {
            'total_credentials': len(self.ledger['credentials']),
            'active_credentials': sum(1 for c in self.ledger['credentials'] if c['status'] == 'active'),
            'ledger_created': self.ledger['metadata']['created_at'],
            'credentials_by_employee': {}
        }
        
        # Group by employee
        for record in self.ledger['credentials']:
            emp_id = record['data']['employee_id']
            if emp_id not in report['credentials_by_employee']:
                report['credentials_by_employee'][emp_id] = []
            
            report['credentials_by_employee'][emp_id].append({
                'credential_id': record['credential_id'],
                'course_name': record['data']['course_name'],
                'completion_date': record['data']['completion_date'],
                'hash': record['hash'][:16] + '...',
                'verified': True
            })
        
        # Save report
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Verification report saved to {output_path}")
        return report

