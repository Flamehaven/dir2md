"""License and feature gating for dir2md open-core model"""
import os
from typing import Set

class LicenseManager:
    """Manages feature access based on license type"""
    
    def __init__(self):
        self.license_key = os.environ.get('DIR2MD_LICENSE', '')
        self.is_pro = self._validate_license()
    
    def _validate_license(self) -> bool:
        """Validate license key (simplified for demo)"""
        # In production, this would validate ed25519 signature
        return self.license_key.startswith('PRO-') and len(self.license_key) > 10
    
    def get_available_features(self) -> Set[str]:
        """Return set of available features based on license"""
        base_features = {
            'basic_masking',
            'directory_scan', 
            'gitignore_filter',
            'token_estimation',
            'simhash_dedup',
            'manifest_json',
            'deterministic_output',
            'basic_stats'
        }
        
        if self.is_pro:
            pro_features = {
                'advanced_masking',
                'language_plugins',
                'parallel_processing', 
                'incremental_cache',
                'drift_comparison',
                'html_pdf_export',
                'pr_integration',
                'tui_interface'
            }
            return base_features.union(pro_features)
        
        return base_features
    
    def check_feature(self, feature: str) -> bool:
        """Check if a feature is available"""
        return feature in self.get_available_features()
    
    def require_pro(self, feature: str) -> None:
        """Raise error if pro feature is accessed without license"""
        if not self.check_feature(feature):
            raise LicenseError(
                f"Feature '{feature}' requires dir2md Pro license. "
                f"Visit https://dir2md.com/pro for more information."
            )

class LicenseError(Exception):
    """Raised when trying to access pro features without license"""
    pass

# Global license manager instance
license_manager = LicenseManager()