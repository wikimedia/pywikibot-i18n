/*!
 * Grunt file
 */

/*jshint node:true */
module.exports = function ( grunt ) {
	grunt.loadNpmTasks( 'grunt-banana-checker' );

	grunt.initConfig( {
		banana: {
			pywikibot: 'pywikibot/',
			thirdparty: 'thirdparty/',
			add_text: 'add_text/',
			archivebot: 'archivebot/',
			basic: 'basic/',
			blockpageschecker: 'blockpageschecker/',
			capitalize_redirects: 'capitalize_redirects/',
			casechecker: 'casechecker/',
			catall: 'catall/',
			category: 'category/',
			category_redirect: 'category_redirect/',
			clean_sandbox: 'clean_sandbox/',
			commons_link: 'commons_link/',
			commons: 'commons/',
			cosmetic_changes: 'cosmetic_changes/',
			delete: 'delete/',
			djvutext: 'djvutext/',
			editarticle: 'editarticle/',
			featured: 'featured/',
			fixing_redirects: 'fixing_redirects/',
			followlive: 'followlive/',
			interwiki: 'interwiki/',
			isbn: 'isbn/',
			lonelypages: 'lonelypages/',
			makecat: 'makecat/',
			misspelling: 'misspelling/',
			movepages: 'movepages/',
			ndashredir: 'ndashredir/',
			noreferences: 'noreferences/',
			pagefromfile: 'pagefromfile/',
			piper: 'piper/',
			protect: 'protect/',
			redirect: 'redirect/',
			reflinks: 'reflinks/',
			remove_edp_images: 'remove_edp_images/',
			replace: 'replace/',
			revertbot: 'revertbot/',
			selflink: 'selflink/',
			solve_disambiguation: 'solve_disambiguation/',
			spamremove: 'spamremove/',
			spellcheck: 'spellcheck/',
			table2wiki: 'table2wiki/',
			template: 'template/',
			undelete: 'undelete/',
			unprotect: 'unprotect/',
			unlink: 'unlink/',
			// Missing messages: weblinkchecker: 'weblinkchecker/',
			welcome: 'welcome/'
		}
	} );

	grunt.registerTask( 'lint', ['banana'] );
	grunt.registerTask( 'test', ['lint'] );
	grunt.registerTask( 'default', ['test'] );
};
